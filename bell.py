__author__ = 'Sam Whitehall'
__license__ = 'MIT'
__version__ = '0.9'

import ast

from IPython.core.error import UsageError
from IPython.core.magic import magics_class, line_cell_magic
from IPython.core.magics.execution import ExecutionMagics

@magics_class
class BellMagic(ExecutionMagics):

    # define line and cell magic (%bell and %%bell)
    @line_cell_magic
    def bell(self, line='', cell=None):
        '''A magic for iPython which notifies the user when the line/cell has
        finished execution.'''

        opts, stmt = self.parse_options(line, 'n:', strict=False)
        notification_type = getattr(opts, 'n', 'bell')
        
        if stmt=="" and cell is None:
            raise UsageError("Can't use statement directly after '%%bell'!")

        # why?
        if cell:
            expr = self.shell.input_transformer_manager.transform_cell(cell)
        else:
            expr = self.shell.input_transformer_manager.transform_cell(line)

        expr_ast = ast.parse(expr)
        expr_ast = self.shell.transform_ast(expr_ast) # why?

        if len(expr_ast.body)==1 and isinstance(expr_ast.body[0], ast.Expr):
            mode = 'eval'
            source = '<bell eval>'
            expr_ast = ast.Expression(expr_ast.body[0].value)
        else:
            mode = 'exec'
            source = '<bell exec>'

        code = compile(expr_ast, source, mode)
        
        if mode=='eval':
            out =  eval(code)
        else:
            # nothing output: is this desirable behaviour?
            exec code
            out = None

        if notification_type == "bell":
            print "\a"

        elif notification_type == "osxbeep":
            try:
                from AppKit import NSBeep
                NSBeep()
            except ImportError:
                raise ImportError("Could not import AppKit.NSBeep -- maybe you're"
                    "not on OS X, or are on an old version without PyObjC")

        elif notification_type == "nc":
            osx_notify(expr, out, sound=True)
            
        elif notification_type == "ncsilent":
            osx_notify(expr, out, sound=False)

        return out


def osx_notify(expr, out, sound=True):
    import sys
    import Foundation, AppKit, objc

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

ip = get_ipython()
ip.register_magics(BellMagic)
