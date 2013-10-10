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
    
    def test_realtions(self):
        """Tokens should be accessible from user object as well as user from token."""
        sessionmaker = Backend.instance().get_sessionmaker()
        session = sessionmaker()
        user = self.User("name")
        session.add(user)
        user.tokens.append(self.Token(user))
        session.add(user)
        session.flush()
        self.assertEqual(len(user.tokens),1)
        self.assertEqual(user.tokens[0].user,user)

if __name__ == '__main__':
    unittest.main()
