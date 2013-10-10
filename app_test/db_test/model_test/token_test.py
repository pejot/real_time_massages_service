#!/usr/bin/env python
import unittest
import os
import sys
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from app_test.base_test_case import BaseTestCase
from db.backend import Backend


class TokenTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(TokenTestCase, self).setUpClass()
        from db.model.token import Token as TokenClass
        from db.model.user import User as UserClass
        self.Token = TokenClass
        self.User = UserClass

    def test_constructor(self):
        """Should generate uuid token and store user correctly."""
        user = self.User("name")
        sessionmaker = Backend.instance().get_sessionmaker()
        session = sessionmaker()
        session.add(user)
        session.flush()
        token = self.Token(user)
        self.assertIsNotNone(token.id)
        self.assertIsNotNone(token.user_id)
        self.assertEquals(user.id, token.user_id)

    def test_constructor_no_param(self):
        """Should rise exception if no user is given."""
        self.assertRaises(TypeError, self.Token)
        print self.Token.user.property

    def test_constructor_none_user_id(self):
        """Should rise exception if no user is given."""
        user = self.User("name")
        self.assertRaises(ValueError, self.Token,user)


if __name__ == '__main__':
    unittest.main()
