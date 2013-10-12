#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from app_test.base_test_case import BaseTestCase
from db.backend import Backend
import unittest


class BackendTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(BackendTestCase, self).setUpClass()
        self.backend = Backend.instance()

    def test_get_metadata(self):
        """Should return always this same and not None instance of metadata."""
        self.assertIsNotNone(self.backend.get_metadata())
        self.assertEqual(
            self.backend.get_metadata(), self.backend.get_metadata())

    def test_get_sessionmaker(self):
        """Should return always this same and not None instance of sessionmaker."""
        self.assertIsNotNone(self.backend.get_sessionmaker())
        self.assertEqual(
            self.backend.get_sessionmaker(), self.backend.get_sessionmaker())

    def test_get_engine(self):
        """Should return always this same not None instance of engine."""
        self.assertIsNotNone(self.backend.get_engine())
        self.assertEqual(self.backend.get_engine(), self.backend.get_engine())

    def test_get_base(self):
        """Should return always this same not None instance of base."""
        self.assertIsNotNone(self.backend.get_base())
        self.assertEqual(self.backend.get_base(), self.backend.get_base())


if __name__ == '__main__':
    unittest.main()
