__author__ = 'Sam Whitehall'
__license__ = 'MIT'
__version__ = '0.9'

import ast
import notifiers

from IPython.core.error import UsageError
from IPython.core.magic import magics_class, line_cell_magic
from IPython.core.magics.execution import ExecutionMagics

notifiers = {
    'term' : notifiers.TerminalBell(),
    'osx' : notifiers.NSBeep(),
    'nc' : notifiers.OSXNotificationCentre()
}

@magics_class
class BellMagic(ExecutionMagics):

    # define line and cell magic (%bell and %%bell)
    @line_cell_magic
    def bell(self, line='', cell=None):
        '''A magic for iPython which notifies the user when the line/cell has
        finished execution.'''

        # parse into notification type option (-n) and statement to execute
        opts, stmt = self.parse_options(line, 'n:', strict=False)
        notify_type = getattr(opts, 'n', 'term')
        # TODO: what about if a user types an incorrect name in?

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
        notifier = notifiers[notify_type]
        notifier.ping(expr, out)
        
        return out

# hook into iPython
ip = get_ipython()
ip.register_magics(BellMagic)
