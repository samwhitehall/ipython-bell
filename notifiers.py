class TerminalBell:
    def ping(self, expr, out):
        #TODO: use system out to avoid extra newline
        print '\a'

class NSBeep:
    def ping(self, expr, out):
        try:
            from AppKit import NSBeep
            NSBeep()
        except ImportError:
            # TODO: what does this error handling look like?
            raise Exception("Could not import AppKit.NSBeep -- maybe you're"
                "not on OS X, or are on an old version without PyObjC")

class OSXNotificationCentre:
    def ping(self, expr, out, sound=True):
        import sys
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

