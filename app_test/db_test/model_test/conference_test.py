#!/usr/bin/env python
import unittest
import os
import sys
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from app_test.base_test_case import BaseTestCase


class ConferenceTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(ConferenceTestCase, self).setUpClass()
        from db.model.conference import Conference as ConferenceClass
        from db.model.user import User as UserClass
        self.Conference = ConferenceClass
        self.User = UserClass

    def test_constructor(self):
        """Default constructor should create conference object."""
        conference = self.Conference()
        self.assertIsNotNone(conference)

    def test_participants(self):
        """Should correctly registed participants"""

        assert False

if __name__ == '__main__':
    unittest.main()
