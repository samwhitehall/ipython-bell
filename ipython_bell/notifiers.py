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

    def linux(self, title, text):
        self.ping(out)

    def windows(self, title, text):
        raise NotImplementedError('Cannot do terminal bell on Windows')


class Say:
    """System beep."""

    def osx(self, title, text):
        os.system("osascript -e 'beep'")
        os.system("say 'Task complete'")

    def linux(self, title, text):
        os.system("beep")
        os.system("spd-say 'Task Complete'")

    def windows(self, title, text):
        try:
            import winsound
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        except ImportError:
            raise Exception('winsound not installed')


class Notification:
    """Send a full notification."""
    sound = True

    def osx(self, title, text):
        applescript = ('display notification "{}" with title "{}"').format(text, title)
        if self.sound:
            applescript += ' sound name "default"'

        command = "osascript -e '{}'".format(applescript)
        os.system(command)

    def linux(self, title, text):
        if output.success:
            text = 'IPython Task Complete'
        else:
            text = output.error_in_exec.__class__.__name__

        command = "notify-send '{}' -h '{}'".format(title, text)
        os.system(command)

        if self.sound:
            os.system("beep")

    def windows(self, title, text):
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, text)
        except ImportError:
            raise Exception('win10toast not installed')


class SilentNotification(Notification):
    sound = False
