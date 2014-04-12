''' notifiers.py : contains separated code for actually performing the 
notification itself.'''

import sys

class TerminalBell:
    '''Default choice to print an audible bell character to stdout. Works in
    terminal IPython and IPython QT, but not in IPython Notebook.'''

    def ping(self, expr, out):
        sys.stdout.write('\a')

class NSBeep:
    '''System beep (OS X only).'''
    def ping(self, expr, out):
        try:
            from AppKit import NSBeep
            NSBeep()
        except ImportError:
            raise Exception("Could not import AppKit.NSBeep -- maybe you're"
                "not on OS X, or are on an old version without PyObjC")

class OSXNotificationCentre:
    '''Send a full notification to OS X Notification Centre (OS X 10.8+)'''
    def ping(self, expr, out, sound=True):
        import Foundation, AppKit, objc # TODO: graceful error handling

        NSUserNotification = objc.lookUpClass('NSUserNotification')
        NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')

        notification = NSUserNotification.alloc().init()
        notification.setTitle_('iPython Task Complete')
        notification.setSubtitle_(expr.split('\n')[0])
        notification.setInformativeText_('stdout: %s' % out) # or stderr in red?
        notification.setUserInfo_({})
        if sound:
            notification.setSoundName_('NSUserNotificationDefaultSoundName')

        NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)

        return None

