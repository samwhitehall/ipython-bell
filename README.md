## About
IPython Bell is a simple magic for IPython and Jupyter Notebooks, which notifies yoy when the current line/cell has finished execution. This is particularly useful for long tasks. It can make sounds or even make notification bubbles pop up.

## Installation
IPython bell can be installed as a standard Python package: either from PyPI:

    pip install IPythonBell

or from git:
    
    git clone http://github.com/samwhitehall/ipython-bell.git 
    cd ipython-bell/
    python setup.py install
    
This can be imported into an IPython shell session using either: `import ipython_bell` or `%load_ext ipython_bell`
    
Although you probably want it to load when IPython loads, in which case, edit your IPython profile file (by default `~/.ipython/profile_default/ipython_config.py`)
and add `ipython_bell` to :

    c.TerminalIPythonApp.extensions = [
        'ipython_bell'
    ]

(you may need to create this, and can do so with `ipython profile create`).

## Usage
This can be used as a magic for a single line (line magic):

    In [1]: %bell print 'hello'
    hello

or across multiple lines (cell magic):

    In[2]: %%bell
    import time
    time.sleep(5)
    
There are four currently available notifiers, selectable with the `-n` or `--notifier` arguments:
* **Terminal Bell** `term` -- prints an audible bell character to `stdout` (doesn't work in Notebook).
* **Say** `say` -- play a system sound & use text-to-speech.
* **Notification** `notify` -- (default) operating system notification with sound
* **Silent Notification** `notify-silent` -- operating notification without
  sound

**MacOS**: should work out of the box.

**Linux**: you may need to install `beep` and/or `libnotify` on Linux.

**Windows**: this is *entirely untested*, so please create an issue (notifications probably only work on Windows 10+).

Specified as follows (in this case, for Notification Center):

    In [1]: %bell -n notify print 'hello'
    hello

    In[2]: %%bell -n notify
    import time
    time.sleep(5)
