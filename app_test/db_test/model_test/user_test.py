#!/usr/bin/env python
import unittest
import os
import sys
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from app_test.base_test_case import BaseTestCase
from db.backend import Backend


class UserTestCase(BaseTestCase):

    username = "name"

    @classmethod
    def setUpClass(self):
        super(UserTestCase, self).setUpClass()
        # to first lets load configuration hide imports
        from db.model.user import User as UserClass
        self.User = UserClass

    def test_constructor(self):
        """Should store name correctly."""
        user = self.User(self.username)
        self.assertEquals(self.username, user.name)

    def test_constructor_no_param(self):
        """Should rise exception if no name is given."""
        self.assertRaises(TypeError, self.User)

    def test_constructor_none_name(self):
        """Should rise exception if there is none name."""
        self.assertRaises(ValueError, self.User, None)
    
    def test_constructor_empty_name(self):
        """Should rise exception if there is none name."""
        self.assertRaises(ValueError, self.User, "")

    def test_constructor_whitespace_name(self):
        """Should rise exception if there is none name."""
        self.assertRaises(ValueError, self.User, " ")

    def test_save(self):
        """Should generate id."""
        user = self.User(self.username)
        sessionmaker = Backend.instance().get_sessionmaker()
        session = sessionmaker()
        session.add(user)
        session.flush()
        self.assertEquals(self.username, user.name)
        self.assertIsNotNone(user.id)
        session.close()

if __name__ == '__main__':
    unittest.main()
