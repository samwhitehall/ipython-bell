from distutils.core import setup

setup(
    name='IPythonBell',
    version='0.9.2',
    packages=['ipython_bell',],
    license='MIT',
    author='Sam Whitehall',
    author_email='me@samwhitehall.com',
    url='http://www.github.com/samwhitehall/ipython-bell',
    description='Python line & cell magic to notify the programmer when a '
        'line/cell has completed execution',
    keywords='ipython jupyter notebook notification notification complete alert',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Framework :: IPython',
        'Natural Language :: English',
        'Topic :: Utilities',
    ],
    requires=[
        'IPython (>=1.00)',
    ],
)
