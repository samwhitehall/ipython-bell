from distutils.core import setup

setup(
    name='IPythonBell',
    version='0.9.1',
    packages=['ipybell',],
    license='MIT',
    author='Sam Whitehall',
    author_email='me@samwhitehall.com',
    url='http://www.github.com/samwhitehall/ipython-bell',
    description='Python line & cell magic to notify the programmer when a '
        'line/cell has completed execution',
    requires=[
        'IPython (>=1.00)',
    ],
)
