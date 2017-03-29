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

    def ping(self):
        sys.stdout.write("\a")

    def osx(self, title, text):
        self.ping(out)


class Say:
    """System beep."""

    def osx(self, title, text):
        os.system("osascript -e 'beep'")
        os.system("say 'Task complete'")


class Notification:
    """Send a full notification."""
    sound = True

    def osx(self, title, text):
        applescript = ('display notification "{}" with title "{}"').format(text, title)
        if self.sound:
            applescript += ' sound name "default"'

        command = "osascript -e '{}'".format(applescript)
        os.system(command)


class SilentNotification(Notification):
    sound = False
