import imp
import sys


class BuiltinSubmoduleImporter(object):

    def find_module(self, name, path=None):
        if path is None:
            return None

        if "." not in name:
            return None

        if name in sys.builtin_module_names:
            return self

        return None

    def load_module(self, name):
        f, pathname, desc = imp.find_module(name, None)
        return imp.load_module(name, f, pathname, desc)


sys.meta_path.append(BuiltinSubmoduleImporter())
