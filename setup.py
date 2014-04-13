from distutils.core import setup

setup(
    name='IPythonBell',
    version='0.9',
    packages=['ipythonbell',],
    license='MIT',
    author='Sam Whitehall',
    author_email='me@samwhitehall.com',
    description='Python line & cell magic to notify the programmer when a '
        'line/cell has completed execution',
    requires=[
        'IPython (>=1.00)',
    ],
)
