''' notifiers.py : contains separated code for actually performing the 
notification itself.'''

import sys

class TerminalBell:
    '''Default choice to print an audible bell character to stdout. Works in
    terminal IPython and IPython QT, but not in IPython Notebook.'''

    def ping(self, expr, out, exception=None):
        sys.stdout.write('\a')

class NSBeep:
    '''System beep (OS X only).'''
    def ping(self, expr, out, exception=None):
        try:
            from AppKit import NSBeep
            NSBeep()
        except ImportError:
            raise Exception("Could not import AppKit.NSBeep -- maybe you're"
                "not on OS X, or are on an old version without PyObjC")

class OSXNotificationCentre:
    '''Send a full notification to OS X Notification Centre (OS X 10.8+)'''
    sound = True
    def ping(self, expr, out, exception=None):
        try:
            import Foundation, AppKit, objc
        except ImportError:
            raise Exception("Could not import Foundation/AppKit/objc -- maybe"
                "you're not on OS X 10.8+")

        NSUserNotification = objc.lookUpClass('NSUserNotification')
        NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')

        notification = NSUserNotification.alloc().init()
        if exception:
            notification.setTitle_('%s in iPython Task' 
                % str(exception.__class__.__name__))
            notification.setInformativeText_(str(exception)) 
        else:
            notification.setTitle_('iPython Task Complete')
            notification.setInformativeText_(out) 
        notification.setSubtitle_(expr.split('\n')[0])
        notification.setUserInfo_({})
        if self.sound:
            notification.setSoundName_('NSUserNotificationDefaultSoundName')

        NSUserNotificationCenter\
            .defaultUserNotificationCenter()\
            .scheduleNotification_(notification)

        return None

class OSXNotificationCentreSilent(OSXNotificationCentre):
    sound = False
