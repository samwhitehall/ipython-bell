"""
Contains separate handlers performing the notification itself.
"""

import os
import sys

class TerminalBell:
    """
    Default choice to print an audible bell character to stdout. Works in
    terminal IPython and IPython QT, but not in IPython Notebook.
    """

    def ping(self, out, exception=None):
        sys.stdout.write("\a")


class Say:
    """System beep."""
    def ping(self, out, exception=None):
        os.system("osascript -e 'beep'")
        os.system("say 'Task complete'")


class Notification:
    """Send a full notification."""
    sound = True

    def ping(self, output):
        if output.success:
            title = 'IPython Task Complete'
            text = output.result or ''
        else:
            exception = output.error_in_exec
            title = '{} in IPython Task'.format(exception.__class__.__name__)
            text = exception.message

        applescript = ('display notification "{}" with title "{}"').format(text, title)
        if self.sound:
            applescript += ' sound name "default"'

        command = "osascript -e '{}'".format(applescript)
        os.system(command)


class SilentNotification(Notification):
    sound = False
