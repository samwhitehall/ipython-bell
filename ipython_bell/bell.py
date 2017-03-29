__author__ = 'Sam Whitehall'
__license__ = 'MIT'
__version__ = '0.9'

import ast
import platform

from ipython_bell import notifiers

from IPython.core.error import UsageError
from IPython.core.magic import magics_class, line_cell_magic
from IPython.core.magics.execution import ExecutionMagics
from IPython.core.magic_arguments import (argument, magic_arguments,
    parse_argstring)

notifiers = {
    'term' : notifiers.TerminalBell(),
    'say' : notifiers.Say(),
    'notify' : notifiers.Notification(),
    'notify-silent' : notifiers.SilentNotification()
}

method_for_platform = {
    'Darwin': 'osx',
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
            notifier = notifiers['term']

        if cell:
            code = cell
        else:
            code = ' '.join(args.statement)

        output = self.shell.run_cell(code)

        if output.success:
            title = 'IPython Task Complete'
            text = output.result or ''
        else:
            exception = output.error_in_exec
            title = '{} in IPython Task'.format(exception.__class__.__name__)
            text = exception.message

        method_name = method_for_platform.get(platform.system())
        if method_name is None:
            raise NotImplementedError('Unsupported Platform')

        # call platform appropriate method
        getattr(notifier, method_name)(title, text)


# hook into iPython
ip = get_ipython()
ip.register_magics(BellMagic)
