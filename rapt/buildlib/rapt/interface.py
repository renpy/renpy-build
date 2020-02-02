import webbrowser
import textwrap
import sys
import time
import subprocess
import urllib

from . import plat

import colorama
from colorama import Fore, Back, Style

colorama.init()


class Interface(object):

    def write(self, s, style=""):
        """
        Writes out s, in the given style and color.
        """

        wrapped = "\n\n".join("\n".join(textwrap.wrap(i)) for i in s.split("\n\n"))

        sys.stdout.write(style)
        sys.stdout.write(wrapped)
        sys.stdout.write(Fore.RESET + Back.RESET + Style.RESET_ALL)
        sys.stdout.write("\n")
        sys.stdout.flush()

    def info(self, prompt):
        """
        Displays `prompt` as an informational message.
        """

        print
        self.write(prompt, Style.BRIGHT)
        print

    def success(self, prompt):
        """
        Displays `prompt` as a success message.
        """

        print
        self.write(prompt, Fore.GREEN + Style.BRIGHT)
        print

    def final_success(self, prompt):
        """
        Displays `prompt` as the last success message of an operation.
        """

        print
        self.write(prompt, Fore.GREEN + Style.BRIGHT)
        print

    def yesno(self, prompt):
        """
        Prompts the user for a response to a yes or no question.
        """

        return self.yesno_choice(prompt)

    def yesno_choice(self, prompt, default=None):
        """
        Prompts the user for a response to a yes or no question.

        This can also take a default, and indicates which of yes or no
        is currently selected, if any.
        """

        print
        self.write(prompt, Style.BRIGHT)

        while True:

            if default is True:
                prompt = "yes/no [yes]> "
            elif default is False:
                prompt = "yes/no [no]> "
            else:
                prompt = "yes/no> "

            choice = raw_input(prompt)
            choice = choice.strip().lower()

            if choice == "yes" or choice == "y":
                return True
            elif choice == "no" or choice == "n":
                return False
            elif choice == "" and default is not None:
                return default

        print

    def terms(self, url, prompt):
        """
        Displays `url` to the user, and then prompts the user to accept the
        terms and conditions.

        If the user doesn't accept, gives up.
        """

        self.info("Opening {} in a web browser.".format(url))

        webbrowser.open_new(url)
        time.sleep(.5)

        if not self.yesno(prompt):
            self.fail("You must accept the terms and conditions to proceed.")

    def input(self, prompt, empty=None): # @ReservedAssignment
        """
        Prompts the user for input. The input is expected to be a string, which
        is stripped of leading and trailing whitespace. If `empty` is true,
        empty strings are allowed. Otherwise, they are not.
        """

        print
        self.write(prompt, Style.BRIGHT)

        while True:

            if empty:
                prompt = "[{}]> ".format(empty)
            else:
                prompt = "> "

            rv = raw_input(prompt)
            rv = rv.strip()

            if rv:
                return rv

            if empty is not None:
                return empty

        print

    def choice(self, prompt, choices, default=None):
        """
        Prompts the user with prompt, and then presents him with a list of
        choices.

        `choices`
            A list of (value, label) tuples.

        `default`
            If not None, should be one of the values. The value that we use
            return if the user just hits enter.
        """

        default_choice = None

        print
        self.write(prompt, Style.BRIGHT)

        for i, (value, label) in enumerate(choices):

            i += 1

            if value == default:
                default_choice = i

            self.write("{}) {}".format(i, label), Style.BRIGHT)

        print

        if default_choice is not None:
            prompt = "1-{} [{}]> ".format(len(choices), default_choice)
        else:
            prompt = "1-{}> ".format(len(choices))

        while True:
            try:
                choice = raw_input(prompt).strip()
                if choice:
                    choice = int(choice)
                else:
                    if default_choice:
                        choice = default_choice
                    else:
                        continue
            except:
                continue

            choice -= 1

            if choice >= 0 and choice < len(choices):
                return choices[choice][0]

        print

    def fail(self, prompt):
        """
        Causes the program to terminate with a message, and a failure code.
        """

        print
        self.write(prompt, Fore.RED + Style.BRIGHT)

        sys.exit(-1)

    def call(self, args, cancel=False, use_path=False, yes=False):
        """
        Executes `args` as a program. Raises subprocess.CalledProcessError
        if the program fails.

        `cancel`
            If true, this is an expensive call that the user may be offered
            the opportunity to cancel.

        `use_path`
            If true, searches the system path for the file.

        `yes`
            Repeatedly sends 'y\n' to the command's stdin.
        """

        if yes:
            p = subprocess.Popen(args, cwd=plat.RAPT_PATH, stdin=subprocess.PIPE)

            try:
                while p.poll() is None:
                    time.sleep(.2)
                    p.stdin.write('y\n')
                    p.stdin.flush()
            except:
                pass

            p.wait()

        else:
            subprocess.check_call(args, cwd=plat.RAPT_PATH)

    def download(self, url, dest):
        """
        Downloads `url` to `dest`.
        """

        urllib.urlretrieve(url, dest)

    def background(self, f):
        """
        Runs f in the background, if possible. Returns when f has finished.

        (This is used in the Ren'Py launcher to update the screen while
        expensive operations are occuring.)
        """

        f()
