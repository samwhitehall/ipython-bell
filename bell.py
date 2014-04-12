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

        # parse into notification type option (-n) and statement to execute
        opts, stmt = self.parse_options(line, 'n:', strict=False)
        notification_type = getattr(opts, 'n', 'bell')

        if stmt=="" and cell is None:
            raise UsageError("Can't use statement directly after '%%bell'!")

        if cell: # i.e. cell magic
            expr = self.shell.input_transformer_manager.transform_cell(cell)
        else: # i.e. line magic
            # NB at the moment, this still includes the options crud
            # TODO: see how %time gets past this
            expr = self.shell.input_transformer_manager.transform_cell(line)

        # convert expression to AST & perform transformations
        expr_ast = ast.parse(expr)
        expr_ast = self.shell.transform_ast(expr_ast) #

        # if it's an expression (i.e. to be evaluated instead of executed, like
        # a statement), then further transforms are needed
        if len(expr_ast.body)==1 and isinstance(expr_ast.body[0], ast.Expr):
            mode = 'eval'
            source = '<bell eval>'
            expr_ast = ast.Expression(expr_ast.body[0].value)
        else:
            mode = 'exec'
            source = '<bell exec>'

        code = compile(expr_ast, source, mode)
        
        # evaluate expression & return to user...
        if mode=='eval':
            out =  eval(code)

        # .. or nothing if it's a statement
        else:
            exec code
            out = None

        # perform actual notification
        # TODO: tidy this out!
        if notification_type == "bell": # terminal bell
            print "\a"

        elif notification_type == "osxbeep": # os x notify sound
            try:
                from AppKit import NSBeep
                NSBeep()
            except ImportError:
                raise ImportError("Could not import AppKit.NSBeep -- maybe you're"
                    "not on OS X, or are on an old version without PyObjC")

        elif notification_type == "nc": # os x notification centre
            osx_notify(expr, out, sound=True)
            
        elif notification_type == "ncsilent": # os x notification centre, silent
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

# hook into iPython
ip = get_ipython()
ip.register_magics(BellMagic)
