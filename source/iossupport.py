from pyobjus import autoclass, objc_str

Log = autoclass('Log')

class LogFile(object):

    def __init__(self):
        self.buffer = ''

    def write(self, s):
        s = self.buffer + s
        lines = s.split("\n")
        for l in lines[:-1]:
            Log.log_(l)
        self.buffer = lines[-1]

    def flush(self):
        return

import sys
sys.stdout = sys.stderr = LogFile()

def open_url(url):

    if url.startswith("file:"):
        raise Exception("Opening file urls is not supported: " + url)

    try:
        NSURL = autoclass('NSURL')
        UIApplication = autoclass("UIApplication")

        nsurl = NSURL.URLWithString_(objc_str(url))
        UIApplication.sharedApplication().openURL_(nsurl)
    except:
        import traceback
        traceback.print_exc()
        raise

# webbrowser does weird things by default - it seems to be confused about
# us being on a mac. Overriding these functions fixes the problem.
import webbrowser
webbrowser.open = open_url
webbrowser.open_new = open_url
webbrowser.open_new_tab = open_url
