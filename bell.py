from IPython.core.magic import magics_class, line_cell_magic
from IPython.core.magics.execution import ExecutionMagics

@magics_class
class BellMagic(ExecutionMagics):
    @line_cell_magic
    def bell(self, line='', cell=None):
        '''my line magic'''
        return line

ip = get_ipython()
ip.register_magics(BellMagic)
