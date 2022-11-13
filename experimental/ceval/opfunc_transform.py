#!/usr/bin/env python3


import argparse
import pathlib
import re

class LineList:
    """
    This represents a list of lines, that can be processed in
    different ways.
    """

    def __init__(self, lines):
        self.lines = lines

    def __add__(self, other):
        return LineList(self.lines + other.lines)

    def __iadd__(self, other):
        self.lines += other.lines
        return self

    def consume_to(self, prefix):
        """
        Consume lines until a line starting with `prefix` is found. Returns the
        lines, including the line that's been consumed.

        Returns None if `prefix` doesn't match.
        """

        rv = [ ]

        while self.lines:
            l = self.lines.pop(0)

            rv.append(l)

            if l.startswith(prefix):
                return LineList(rv)

        self.lines = rv
        return None

    def consume_before(self, prefix):
        """
        Consumes lines until a line starting with `prefix` is found. Returns the
        lines, excluding the line that's been consumed.

        Returns None if `prefix` doesn't match.
        """

        rv = [ ]

        while self.lines:
            l = self.lines.pop(0)

            if l.startswith(prefix):
                self.lines.insert(0, l)
                return LineList(rv)

            rv.append(l)

        self.lines = rv
        return None


    def rest(self):
        """
        Return the rest of the lines.
        """

        rv = self.lines
        self.lines = [ ]
        return LineList(rv)


    def removeprefix(self, prefix):
        """
        Modifies this LineList by removing the whitespace found
        on the first line.
        """

        self.lines = [ i.removeprefix(prefix) for i in self.lines ]

    def sub(self, regex, replacement):
        """
        Modifies this LineList by replacing all matches of `regex`
        with `replacement`.
        """

        self.lines = [ re.sub(regex, replacement, i) for i in self.lines ]

    def replace(self, old, new):
        """
        Modifies this LineList by replacing all occurrences of `old`
        with `new`.
        """

        self.lines = [ i.replace(old, new) for i in self.lines ]

    def replace_word(self, old, new):
        """
        Modifies this LineList by replacing all occurrences of `old`
        with `new`, but only if `old` is a whole word.

        This does not match the word if it's preceded by -> or .
        """

        self.lines = [ re.sub(r"(?<!\.)(?<!->)\b{}\b".format(old), new, i) for i in self.lines ]

    def insert_at_start(self, text):
        """
        Inserts `text` at the start of the list.
        """

        self.lines = [ i.rstrip() for i in text.splitlines() ] + self.lines

    def insert_after(self, prefix, text, skip=0):
        """
        Inserts `text` after the first line starting with `prefix`.

        If `skip` is set, skip `skip` lines after the first line that starts
        with `prefix`.
        """

        newlines = [ ]

        while self.lines:
            line = self.lines.pop(0)
            newlines.append(line)

            if line.startswith(prefix):
                break

        for _ in range(skip):
            newlines.append(self.lines.pop(0))

        newlines.extend(i.rstrip() for i in text.splitlines())
        newlines.extend(self.lines)

        self.lines = newlines

    def insert_at_end(self, text):
        """
        Inserts `text` at the start of the list.
        """

        self.lines = self.lines + [ i.rstrip() for i in text.splitlines() ]

    def text(self):
        """
        Return the lines as a single string.
        """

        return "\n".join(self.lines) + "\n"



def handle_target(lb):
    """
    Handle a single TARGET() block.
    """

    name = re.search(r"TARGET\((.*)\)", lb.lines[0]).group(1)
    if name == "MATCH_CLASS":
        lb.replace("ctx->names", "names")

    lb.sub(r"\breturn (.*);", r"ctx->return_value = \1; return opfunc_return_value;")

    lb.sub(r"TARGET\(([^)]+)\)", r"static opfunc_return opfunc_\1(opfunc_ctx *ctx, PyThreadState *tstate, _PyInterpreterFrame *frame)")
    lb.sub(r"\bgoto ", "return opfunc_goto_")

    lb.sub(r"\bDISPATCH\(\)", "return opfunc_goto_dispatch")
    lb.sub(r"\bDISPATCH_GOTO\(\)", "return opfunc_goto_dispatch_goto")
    lb.sub(r"\bDISPATCH_SAME_OPARG\(\)", "return opfunc_goto_dispatch_same_oparg")
    lb.sub(r"\bTRACE_FUNCTION_EXIT\(\)", "return opfunc_goto_trace_function_exit")



    return lb

def handle_eval_frame(lb, opfuncs):

    lb.replace("#define USE_COMPUTED_GOTOS 0", "#define USE_COMPUTED_GOTOS 1")

    lb.replace("int lastopcode = 0;", "")
    lb.replace("uint8_t opcode;", "")
    lb.replace("int oparg;", "")
    lb.replace("int lltrace = 0;", "")
    lb.replace("_PyCFrame cframe;", "")
    lb.replace("PyObject *names;", "")
    lb.replace("PyObject *consts;", "")
    lb.replace("_Py_CODEUNIT *first_instr;", "")
    lb.replace("_Py_CODEUNIT *next_instr;", "")
    lb.replace("PyObject **stack_pointer;", "")
    lb.replace("CallShape call_shape;", "")


    lb.replace_word("lastopcode", "ctx->lastopcode")
    lb.replace_word("opcode", "ctx->opcode")
    lb.replace_word("oparg", "ctx->oparg")
    lb.replace_word("lltrace", "ctx->lltrace")
    lb.replace_word("cframe", "ctx->cframe")
    lb.replace_word("names", "ctx->names")
    lb.replace_word("consts", "ctx->consts")
    lb.replace_word("first_instr", "ctx->first_instr")
    lb.replace_word("next_instr", "ctx->next_instr")
    lb.replace_word("stack_pointer", "ctx->stack_pointer")
    lb.replace_word("eval_breaker", "ctx->eval_breaker")
    lb.replace_word("call_shape", "ctx->call_shape")

    lb.replace("goto miss;", "return opfunc_goto_miss;")

    lb.replace('#include "opcode_targets.h"', "")

    lb.replace("#define is_method(ctx->stack_pointer, args)", "#define is_method(stack_pointer, args)")


    lb.replace(
        "_Py_atomic_int * const ctx->eval_breaker = &tstate->interp->ceval.eval_breaker;",
        "ctx->eval_breaker = &tstate->interp->ceval.eval_breaker;"
    )



    # lb.replace(
    #     "_Py_atomic_int * const ctx->eval_breaker = &tstate->interp->ceval.eval_breaker;

    #     "_Py_atomic_int * const ctx->eval_breaker = &tstate->interp->ceval.ctx->eval_breaker;",
    #     "ctx->eval_breaker = &tstate->interp->ceval->eval_breaker;")


    targets = [ ]

    lines = lb.consume_before("        TARGET(")

    while target := lb.consume_to("        TARGET("):
        target += lb.consume_to("        }")
        lb.consume_before("        TARGET(")
        targets.append(target)

    lines += lb.rest()


    lines.insert_at_start("""
typedef enum {
    opfunc_return_value,
    opfunc_goto_dispatch,
    opfunc_goto_dispatch_goto,
    opfunc_goto_dispatch_same_oparg,
    opfunc_jump_to_instruction,
    opfunc_goto_error,
    opfunc_goto_binary_subscr_dict_error,
    opfunc_goto_call_function,
    opfunc_goto_exception_unwind,
    opfunc_goto_handle_eval_breaker,
    opfunc_goto_resume_frame,
    opfunc_goto_resume_with_error,
    opfunc_goto_start_frame,
    opfunc_goto_unbound_local_error,
    opfunc_goto_miss,
    opfunc_goto_exit_unwind,
    opfunc_goto_do_tracing,
    opfunc_goto_unknown_opcode,
    opfunc_goto_trace_function_exit,
} opfunc_return;


typedef struct {
    PyObject *kwnames;
} CtxCallShape;

typedef struct {
    int lastopcode;
    uint8_t opcode;
    int oparg;
    int lltrace;
    _PyCFrame cframe;
    PyObject *names;
    PyObject *consts;
    _Py_CODEUNIT *first_instr;
    _Py_CODEUNIT *next_instr;
    PyObject **stack_pointer;
    _Py_atomic_int *eval_breaker;

    CtxCallShape call_shape;

    PyObject *return_value;

} opfunc_ctx;

typedef opfunc_return (*opfunc)(opfunc_ctx *ctx, PyThreadState *tstate, _PyInterpreterFrame *frame);

extern opfunc opfuncs[];
""")

    lines.insert_after("_PyEval_EvalFrameDefault(", """

#undef DISPATCH
#define DISPATCH() goto dispatch

#undef DISPATCH_GOTO
#define DISPATCH_GOTO() goto dispatch_goto

    opfunc_ctx opfunc_context;
    opfunc_ctx *ctx = &opfunc_context;

    ctx->lastopcode = 0;
    ctx->lltrace = 0;
""", skip=1)

    lines.insert_at_end("""
#undef PREDICT
#define PREDICT(op)

#undef PREDICTED
#define PREDICTED(op)

#undef CHECK_EVAL_BREAKER
#define CHECK_EVAL_BREAKER() \\
    _Py_CHECK_EMSCRIPTEN_SIGNALS_PERIODICALLY(); \\
    if (_Py_atomic_load_relaxed_int32(ctx->eval_breaker)) { \\
        return opfunc_goto_handle_eval_breaker; \\
    }

#undef JUMP_TO_INSTRUCTION
#define JUMP_TO_INSTRUCTION(op) { ctx->opcode = op; return opfunc_jump_to_instruction; }
""")

    for t in targets:
        t.removeprefix("        ")
        lines += handle_target(t)

    lines.insert_at_end("""
static opfunc_return opfunc_unknown_opcode(opfunc_ctx *ctx, PyThreadState *tstate, _PyInterpreterFrame *frame) {
    return opfunc_goto_unknown_opcode;
}

static opfunc_return opfunc_DO_TRACING(opfunc_ctx *ctx, PyThreadState *tstate, _PyInterpreterFrame *frame) {
    return opfunc_goto_do_tracing;
}
""")



    lines.insert_at_end("opfunc opfuncs[] = {")

    for i in opfuncs:
        lines.insert_at_end(f"    {i},")

    lines.insert_at_end("};")

    print(lines.text())

    return lines

def opcode_funcs(ceval):
    ceval = pathlib.Path(ceval)
    opcode_targets = ceval.parent / "opcode_targets.h"

    with open(opcode_targets) as f:
        lines = f.readlines()

    lines = [ i.strip() for i in lines ]

    rv = [ ]

    for i in lines:
        i = i.rstrip(",")

        if i.startswith("&&TARGET_"):
            rv.append("opfunc_" + i.removeprefix("&&TARGET_"))
        elif i == "&&_unknown_opcode":
            rv.append("opfunc_unknown_opcode")

    return rv


def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("ceval", help="Path to the ceval.c file to update.")
    args = ap.parse_args()

    with open(args.ceval, "r") as f:
        lines = [ i.rstrip() for i in f.readlines() ]

    opfuncs = opcode_funcs(args.ceval)

    lb = LineList(lines)

    result = lb.consume_to("eval_frame_handle_pending(")
    result += lb.consume_to("}")

    eval_frame = lb.consume_to("_PyEval_EvalFrameDefault(")
    eval_frame += lb.consume_to("}")

    result += handle_eval_frame(eval_frame, opfuncs)

    result += lb.rest()

    with open(args.ceval, "w") as f:
        f.write(result.text())


if __name__ == "__main__":
    main()
