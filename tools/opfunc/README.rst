Opfunc Transform
----------------

This script modifies Python's ceval.c file so that the _PyEval_EvalFrameDefault
function is broken up into smaller per-opcode functions (called opfuncs). The
reason for this is that _PyEval_EvalFrameDefault is so large that web browsers
fail to properly optimize it, which makes it take up so much space on the
stack that a game will run out of memory.

See:

    https://bugs.chromium.org/p/chromium/issues/detail?id=1305848

for a discussion of this. This is a Python 3 point and automation of the
work done for Python 2.7 by Tey, at

    https://github.com/renpy/renpyweb/pull/28
