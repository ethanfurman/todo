import setuptools
from distutils.core import setup
import sys

long_desc = '''\
todo - a simple, personal, command-line todo manager
====================================================

- -a, --add "a task"  add a new todo
- -d, --delete <id>   delete a todo
'''

requirements = ['aenum', 'scription']

py2_only = ()
py3_only = ()
make = []

data = dict(
       name='todo',
       version='0.1.0a1',
       license='BSD License',
       description='a simple command-line todo manager',
       long_description=long_desc,
       long_description_content_type='text/markdown',
       packages=['todo'],
       package_data={
           'todo': [
               'CHANGES',
               'LICENSE',
               ],
           },
       install_requires=requirements,
       author='Ethan Furman',
       author_email='ethan@stoneleaf.us',
       url='https://bitbucket.org/stoneleaf/todo',
       entry_points={
           'console_scripts': ['todo = todo.__main__:Main'],
           },
       classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
		    'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            ],
        )

if __name__ == '__main__':
    setup(**data)
