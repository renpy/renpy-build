#!/usr/bin/env python3


import argparse

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


    def text(self):
        """
        Return the lines as a single string.
        """

        return "\n".join(self.lines) + "\n"



def handle_target(lb):
    """
    Handle a single TARGET() block.
    """

    return lb

def handle_eval_frame(lb):

    targets = [ ]

    lines = lb.consume_before("        TARGET(")


    while target := lb.consume_to("        TARGET("):
        target += lb.consume_to("        }")
        lb.consume_before("        TARGET(")
        targets.append(target)

    lines += lb.rest()

    for t in targets:
        t.removeprefix("        ")
        lines += t

    print(lines.text())
    return lines

def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("ceval", help="Path to the ceval.c file to update.")
    args = ap.parse_args()

    with open(args.ceval, "r") as f:
        lines = [ i.rstrip() for i in f.readlines() ]

    lb = LineList(lines)

    result = lb.consume_to("eval_frame_handle_pending(")
    result += lb.consume_to("}")

    eval_frame = lb.consume_to("_PyEval_EvalFrameDefault(")
    eval_frame += lb.consume_to("}")

    result += handle_eval_frame(eval_frame)

    result += lb.rest()

    with open(args.ceval, "w") as f:
        f.write(result.text())


if __name__ == "__main__":
    main()
