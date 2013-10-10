#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from test.base_test import BaseTest
from db.abstract_backend import AbstractBackend


class AbstractBackendTestCase(BaseTest):

    @classmethod
    def setUpClass(self):
        super(AbstractBackendTestCase, self).setUpClass()
        self.abstract_backend = AbstractBackend()

    def test_get_metadata(self):
        """ As an abstract class should return NotImplementedError"""
        self.assertRaises(
            NotImplementedError, self.abstract_backend.get_metadata)

    def test_get_sessionmaker(self):
        """ As an abstract class should return NotImplementedError """
        self.assertRaises(
            NotImplementedError, self.abstract_backend.get_sessionmaker)

    def test_get_engine(self):
        """ As an abstract class should return NotImplementedError """
        self.assertRaises(
            NotImplementedError, self.abstract_backend.get_engine)

    def test_get_base(self):
        """ As an abstract class should return NotImplementedError """
        self.assertRaises(
            NotImplementedError, self.abstract_backend.get_base)

if __name__ == '__main__':
    unittest.main()
