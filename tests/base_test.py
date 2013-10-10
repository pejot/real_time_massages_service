#!/usr/bin/env python
import os
from tornado.options import parse_config_file
import unittest

class BaseTest(unittest.TestCase):

    """
    Base test for all test - loads all configurations
    """
    @classmethod
    def setUpClass(self):
        config_file = os.path.join(os.path.dirname(__file__), "test.cfg")
        parse_config_file(config_file)
