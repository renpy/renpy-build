import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent, indent
from typing import Iterator


def _find_matching_brace(src: str, open_pos: int) -> int:
    """
    Given the position of an opening '{', return the position of the matching closing '}'.
    """

    depth = 1
    i = open_pos + 1
    n = len(src)
    while i < n and depth > 0:
        ch = src[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        elif ch == "/":
            # Skip // and /* comments
            if i + 1 < n:
                if src[i + 1] == "/":
                    # line comment
                    end = src.find("\n", i + 2)
                    i = end if end != -1 else n
                    continue
                elif src[i + 1] == "*":
                    end = src.find("*/", i + 2)
                    i = end + 2 if end != -1 else n
                    continue
        elif ch == '"':
            # Skip string literal
            i += 1
            while i < n and src[i] != '"':
                if src[i] == "\\":
                    i += 1
                i += 1
        elif ch == "'":
            i += 1
            while i < n and src[i] != "'":
                if src[i] == "\\":
                    i += 1
                i += 1
        i += 1

    if depth != 0:
        raise ValueError(f"Unmatched brace at offset {open_pos}")

    return i - 1


@dataclass
class TargetBlock:
    "One TARGET(name) { ... } block from generated_cases.c.h"

    name: str
    body: str


@dataclass
class LabelBlock:
    "One LABEL(name) { ... } block from generated_cases.c.h"

    name: str
    body: str


def parse_generated_cases(src: str) -> Iterator[TargetBlock | LabelBlock]:
    """Extract every TARGET(NAME) { ... } block from *src*."""

    for m in re.finditer(r"(TARGET|LABEL)\(([A-Za-z_][A-Za-z0-9_]*)\)\s*\{", src):
        kind, name = m.groups()
        open_brace = m.end() - 1
        close_brace = _find_matching_brace(src, open_brace)
        body = dedent(src[open_brace + 1 : close_brace])

        # Exists in INTERPRETER_EXIT opcode and in exit_unwind label.
        if name in ("INTERPRETER_EXIT", "exit_unwind"):
            body = re.sub(
                r"return (.*?);",
                r"ctx->return_value = \1; return opfunc_return_value;",
                body,
            )

        yield (TargetBlock if kind == "TARGET" else LabelBlock)(name=name, body=body)


def generate_handler(block: TargetBlock | LabelBlock) -> str:
    """Generate a handler function for one opcode."""

    result: list[str] = []
    result.append("static _RenPyEvalFuncReturn")
    result.append(f"handler_{block.name}(OPFUNC_PARAMS)")
    result.append("{")

    if isinstance(block, TargetBlock):
        opcode = block.name
    else:
        opcode = "ctx->opcode"

    result.append(f"    int opcode = {opcode};")
    result.append("    (void)(opcode);")

    result.append(indent(block.body, "    "))
    result.append("}")
    result.append("\n")

    return "\n".join(result)


UNIT_CODE = r"""
#ifdef Py_STATS
#error "Py_STATS is not supported in Emscripten asyncify build"
#endif

#ifdef LLTRACE
#error "LLTRACE is not supported in Emscripten asyncify build"
#endif

#ifdef _Py_JIT
#error "JIT is not supported in Emscripten asyncify build"
#endif

#ifdef _Py_TIER2
#error "Tier 2 is not supported in Emscripten asyncify build"
#endif

#if Py_TAIL_CALL_INTERP
#error "Py_TAIL_CALL_INTERP must be 0 for the Emscripten asyncify build"
#endif

#if USE_COMPUTED_GOTOS
#error "USE_COMPUTED_GOTOS must be 0 for the Emscripten asyncify build"
#endif

typedef enum {
    opfunc_return_value = 256,
    opfunc_call_pop_2_error,
    opfunc_call_pop_1_error,
    opfunc_call_error,
    opfunc_call_exception_unwind,
    opfunc_call_exit_unwind,
    opfunc_call_start_frame,
} _RenPyEvalFuncReturn;

typedef struct {
    _PyInterpreterFrame *frame;
    _PyStackRef         *stack_pointer;
    _Py_CODEUNIT        *next_instr;
    int                  opcode;
    int                  oparg;

    PyObject            *return_value;
} _RenPyEvalFuncContext;

#define OPFUNC_PARAMS _PyInterpreterFrame *frame, _PyStackRef *stack_pointer, PyThreadState *tstate, _Py_CODEUNIT *next_instr, int oparg, _RenPyEvalFuncContext *ctx
#define OPFUNC_ARGS frame, stack_pointer, tstate, next_instr, oparg, ctx

typedef _RenPyEvalFuncReturn (*_RenPyEvalFunc)(OPFUNC_PARAMS);

#define WRITE_CONTEXT()                 \
    ctx->frame         = frame;         \
    ctx->stack_pointer = stack_pointer; \
    ctx->next_instr    = next_instr;    \

#undef DISPATCH_GOTO
#define DISPATCH_GOTO()                      \
    do {                                     \
        WRITE_CONTEXT();                     \
        ctx->oparg = oparg;                  \
        return (_RenPyEvalFuncReturn)opcode; \
    } while (0)

#undef JUMP_TO_LABEL
#define JUMP_TO_LABEL(name)             \
    do {                                \
        WRITE_CONTEXT();                \
        return opfunc_call_##name;      \
    } while (0)

#undef JUMP_TO_PREDICTED
#define JUMP_TO_PREDICTED(name)            \
    do {                                   \
        WRITE_CONTEXT();                   \
        ctx->next_instr = this_instr;      \
        return (_RenPyEvalFuncReturn)name; \
    } while (0)

"""

INIT_CONTEXT = """
(void)opcode;
(void)oparg;

_RenPyEvalFuncContext ctx = {
    .frame = frame,
};
int dispatch_code = opfunc_call_start_frame;
"""

DISPATCH_CODE = """
start_frame:
    dispatch_code = opfunc_call_start_frame;
    goto dispatch;

error:
    ctx.next_instr = next_instr;
    ctx.stack_pointer = stack_pointer;
    dispatch_code = opfunc_call_error;
    goto dispatch;

dispatch:
    for (;;) {
        if (dispatch_code == opfunc_return_value) {
            return ctx.return_value;
        }

        dispatch_code = EvalFuncs[dispatch_code](
            ctx.frame,
            ctx.stack_pointer,
            tstate,
            ctx.next_instr,
            ctx.oparg,
            &ctx);
    }
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, help="Path to root of Python source")
    root: Path = parser.parse_args().root

    cases_text = (root / "Python/generated_cases.c.h").read_text()
    cases = list(parse_generated_cases(cases_text))

    # Allow to run this script multiple times
    if not (root / "Python/original_ceval.c").exists():
        (root / "Python/ceval.c").copy(root / "Python/original_ceval.c")

    with open(root / "Python/original_ceval.c", "r") as f:
        src = f.readlines()

    idx = None
    for i, line in enumerate(src):
        if line == "} _PyEntryFrame;\n":
            idx = i + 1
            break

    if idx is None:
        raise ValueError("Malformed ceval.c")

    new_src = src[:idx]

    # File level patch
    new_src.append("\n")
    new_src.append(UNIT_CODE)

    # Opcode and label handlers
    new_src.append("#define TIER_ONE 1\n")
    for block in cases:
        new_src.append(generate_handler(block))
    new_src.append("#undef TIER_ONE\n")

    new_src.append("static const _RenPyEvalFunc EvalFuncs[] = {\n")
    for block in cases:
        if isinstance(block, LabelBlock):
            name = f"opfunc_call_{block.name}"
        else:
            name = block.name
        new_src.append(f"    [{name}] = handler_{block.name},\n")
    new_src.append("};\n\n")

    next_idx = None
    for i, line in enumerate(src):
        if line == "    entry.frame.localsplus[0] = PyStackRef_NULL;\n":
            next_idx = i
            break

    if next_idx is None:
        raise ValueError("Malformed ceval.c")

    new_src.extend(src[idx:next_idx])
    new_src.append(indent(INIT_CONTEXT, "    "))

    idx = next_idx
    next_idx = None
    for i, line in enumerate(src):
        if line == '#   include "generated_cases.c.h"\n':
            next_idx = i
            break

    if next_idx is None:
        raise ValueError("Malformed ceval.c")

    new_src.extend(src[idx:next_idx])

    # Function level patch
    new_src.append(indent(DISPATCH_CODE, "    "))

    # Skip the generated_cases.c.h include
    new_src.extend(src[next_idx + 1 :])

    with open(root / "Python/ceval.c", "w") as f:
        f.writelines(new_src)


if __name__ == "__main__":
    main()
