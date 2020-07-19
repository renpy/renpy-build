import subprocess
import re

def construct_env(c):
    """
    Constructs the emsdk environment.
    """

    c.env("EMSDK_BASH", "1")

    bash = subprocess.check_output([ str(c.path("{{ cross }}/emsdk/emsdk")), "construct_env" ], env=c.environ, text=True, stderr=subprocess.STDOUT)

    for l in bash.split("\n"):
        m = re.match(r'export (\w+)=\"(.*?)\";$', l)
        if m:
            c.env(m.group(1), m.group(2))

def generate_makefile_lines(fn):
    """
    A generator that removes continuation lines from the makefile.
    """

    line = ""

    with open(fn) as f:
        for l in f:
            
            line = line + l.strip()
            
            if line.endswith("\\"):
                line = line[:-1] + " "
            else:
                yield line
                line = ""


def parse_makefile(c):
    """
    Parses renpyweb/Makefile to get variables.
    """

    for l in generate_makefile_lines(c.path("{{ renpyweb }}/Makefile")):
        m = re.match(r'(\w+)\s*=\s*(.*)', l)
        if m is not None:
            print(m.group(1), "->", m.group(2))


def activate(c):
    """
    Reads the configuration from emsdk and renpyweb, and uses it to update
    the environment.
    """

    c.var("renpyweb", "{{ root }}/renpyweb")

    construct_env(c)

    c.env("CFLAGS", "{{ CFLAGS }} -s USE_SDL=2 -s USE_FREETYPE=1")

    # parse_makefile(c)

