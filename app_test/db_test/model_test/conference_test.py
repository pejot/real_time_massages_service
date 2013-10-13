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
        conference = self.Conference()
        user_1 = self.User("user_2")
        user_2 = self.User("user_1")
        self.session.add(conference)
        self.session.flush()
        try:
            conference.participants.append(user_1)
            conference.participants.append(user_2)
            self.assertEqual(2, len(conference.participants))
        finally:
            self.session.delete(conference)


if __name__ == '__main__':
    unittest.main()
