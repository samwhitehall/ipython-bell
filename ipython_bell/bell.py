__author__ = 'Sam Whitehall'
__license__ = 'MIT'
__version__ = '0.9'

import ast
from ipython_bell import notifiers

from IPython.core.error import UsageError
from IPython.core.magic import magics_class, line_cell_magic
from IPython.core.magics.execution import ExecutionMagics
from IPython.core.magic_arguments import (argument, magic_arguments,
    parse_argstring)

notifiers = {
    'term' : notifiers.TerminalBell(),
    'osx' : notifiers.NSBeep(),
    'nc' : notifiers.OSXNotificationCentre(),
    'ncsilent' : notifiers.OSXNotificationCentreSilent()
}

@magics_class
class BellMagic(ExecutionMagics):

    # define line and cell magic (%bell and %%bell)
    @magic_arguments()
    @argument('-n', 
        '--notifier', 
        choices=notifiers.keys(), 
        help='Choice of notifiers')
    @argument('statement', 
        nargs='*', 
        help='')
    @line_cell_magic
    def bell(self, line, cell=None):
        '''A magic for iPython which notifies the user when the line/cell has
        finished execution.'''

        args = parse_argstring(self.bell, line)

        if args.notifier:
            notifier = notifiers[args.notifier]
        else:
            notifier = notifiers['term'] # TODO: some better ability to set defaults 

        if cell:
            code = cell
        else:
            code = ' '.join(args.statement)

        out = self.shell.run_cell(code)
        notifier.ping(code, out)
                
        return out

# hook into iPython
ip = get_ipython()
ip.register_magics(BellMagic)
