#!/usr/bin/env python
import os
from tornado.options import parse_config_file, define, options
import unittest
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(APP_ROOT))


class BaseTest(unittest.TestCase):

    """
    Base test for all test - loads all configurations and adds app to sys path
    """
    @classmethod
    def setUpClass(self):
        if "port" not in options:
            define("port", default=8888, type=int)
        if "db" not in options:
            define("db", default=":memory:")
        config_file = os.path.join(os.path.dirname(__file__), "test.cfg")
        parse_config_file(config_file)