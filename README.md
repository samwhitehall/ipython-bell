## About
IPython Bell is a simple magic for IPython, which notifies the user when the current line/cell has finished execution. This is particularly useful for long tasks. This also works in IPython QT and IPython Notebook. It can also notify you via. OS X Notification Center.

## Installation
IPython bell can be installed as a standard Python package: either from PyPI:

    pip install IPythonBell

or from git:
    
    git clone http://github.com/samwhitehall/ipython-bell.git 
    cd ipython-bell/
    python setup.py install
    
This can be imported into an IPython shell session using either: `import ipybell` or `%load_ext ipybell`
    
Although you probably want it to load when IPython loads, in which case, edit your IPython profile file (by default `~/.ipython/profile_default/ipython_config.py`)
and add `ipybell` to :

    c.TerminalIPythonApp.extensions = [
        'ipybell'
    ]

(you may need to create this).

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
* **Mac System Beep** `osx` -- system beep (Mac OS X only).
* **Notification Center** `nc` -- Notification Center (Mac OS X 10.8+ only)
* **Notification Center (silent)** `ncsilent` -- Notification Center, just popup (Mac OS X 10.8+ only)

Specified as follows (in this case, for Notification Center):

    In [1]: %bell -n nc print 'hello'
    hello

    In[2]: %%bell -n nc
    import time
    time.sleep(5)
