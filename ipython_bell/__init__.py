from ipython_bell import bell
def load_ipython_extension(ipython):
    ipython.register_magics(bell.BellMagic)
