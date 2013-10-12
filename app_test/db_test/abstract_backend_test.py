#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from app_test.base_test_case import BaseTestCase
from db.abstract_backend import AbstractBackend


class AbstractBackendTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(AbstractBackendTestCase, self).setUpClass()

    def test_abstract_nature(self):
        """Abstract class shouldn't be initalize."""
        self.assertRaises(
            TypeError, AbstractBackend)

if __name__ == '__main__':
    unittest.main()
