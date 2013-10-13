#!/usr/bin/env python
import unittest
import os
import sys
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from app_test.base_test_case import BaseTestCase


class ConferencesUsersTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(ConferencesUsersTestCase, self).setUpClass()
        from db.model.conference import Conference
        from db.model.user import User
        self.Conference = Conference
        self.User = User

    def setUp(self):
        super(ConferencesUsersTestCase, self).setUp()
        self.user_1 = self.User("name_1")
        self.user_2 = self.User("name_2")
        self.conference = self.Conference()
        self.session.add(self.user_1)
        self.session.add(self.user_2)
        self.session.add(self.conference)
        self.session.flush()

    def tearDown(self):
        self.session.delete(self.user_1)
        self.session.delete(self.user_2)
        self.session.delete(self.conference)
        self.session.flush()
        super(ConferencesUsersTestCase, self).tearDown()

    def test_conference_participants(self):
        self.conference.participants.append(self.user_1)
        self.conference.participants.append(self.user_2)
        self.assertEqual(2, len(self.conference.participants))
        self.assertEqual(1, len(self.user_1.conferences))
        self.assertEqual(1, len(self.user_2.conferences))

    def stest_users_conferences(self):
        self.user_1.conferences.append(self.user_1)
        self.user_2.conferences.append(self.user_2)
        self.assertEqual(2, len(self.conference.participants))
        self.assertEqual(1, len(self.user_1.conferences))
        self.assertEqual(1, len(self.user_2.conferences))

if __name__ == '__main__':
    unittest.main()
