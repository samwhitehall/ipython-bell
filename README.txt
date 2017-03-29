## About
IPython Bell is a simple magic for IPython, which notifies the user when the current line/cell has finished execution. This is particularly useful for long tasks. This also works in IPython and Jupyter Notebooks. It can also notify you via. OS X Notification Center.

## Installation
IPython bell can be installed as a standard Python package: either from PyPI:

    pip install ipython-bell

or from git:
    
    git clone http://github.com/samwhitehall/ipython-bell.git 
    cd ipython-bell/
    python setup.py install
    
This can be imported into an IPython shell session using either: `import ipybell` or `%load_ext ipython_bell`
    
Although you probably want it to load when IPython loads, in which case, edit your IPython profile file (by default `~/.ipython/profile_default/ipython_config.py`)
and add `ipython_bell` to :

    c.TerminalIPythonApp.extensions = [
        'ipython_bell'
    ]

(you may need to create this, using `ipython profile create`).

## Usage
This can be used as a magic for a single line (line magic):

    In [1]: %bell print 'hello'
    hello

or across multiple lines (cell magic):

    In[2]: %%bell
    import time
    time.sleep(5)
    
There are four currently available notifiers, selectable with the `-n` or `--notifier` arguments:
* **Terminal Bell** `term` -- (default) prints an audible bell character to `stdout` (doesn't work in Notebook).
* **Mac System Beep** `say` -- system beep (Mac OS X only).
* **Notification Center** `notify` -- Notification Center (Mac OS X 10.8+ only)
* **Notification Center (silent)** `notify-silent` -- Notification Center, just popup (Mac OS X 10.8+ only)

Specified as follows (in this case, for Notification Center):

    In [1]: %bell -n notify print 'hello'
    hello

    In[2]: %%bell -n notify
    import time
    time.sleep(5)
