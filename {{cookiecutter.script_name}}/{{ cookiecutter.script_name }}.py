#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''{{ cookiecutter.script_name }}

Usage:
  {{ cookiecutter.script_name }} ship new <name>...
  {{ cookiecutter.script_name }} ship <name> move <x> <y> [--speed=<kn>]
  {{ cookiecutter.script_name }} ship shoot <x> <y>
  {{ cookiecutter.script_name }} mine (set|remove) <x> <y> [--moored|--drifting]
  {{ cookiecutter.script_name }} -h | --help
  {{ cookiecutter.script_name }} --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
'''

from __future__ import unicode_literals, print_function
from docopt import docopt

__version__ = "{{ cookiecutter.version }}"
__author__ = "{{ cookiecutter.full_name }}"
__license__ = "MIT"


def main():
    '''Main entry point for the {{ cookiecutter.script_name }} CLI.'''
    args = docopt(__doc__, version=__version__)
    print(args)

if __name__ == '__main__':
    main()