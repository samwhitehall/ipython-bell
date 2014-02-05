from IPython.core.magic import register_line_magic

@register_line_magic
def mylmagic(line):
    '''my line magic'''
    return line
