# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from nose.tools import *  # PEP8 asserts
from subprocess import check_output


class Test{{ cookiecutter.script_name }}(unittest.TestCase):

    '''Unit tests for {{cookiecutter.script_name }}.'''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_echo(self):
        '''An example test.'''
        result = run_cmd("echo hello world")
        assert_equal(result, "hello world\n")

def run_cmd(cmd):
    '''Run a shell command `cmd` and return its output.'''
    return check_output(cmd, shell=True).decode('utf-8')


if __name__ == '__main__':
    unittest.main()