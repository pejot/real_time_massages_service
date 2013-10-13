#!/usr/bin/env python
import unittest
import os
import sys
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from app_test.base_test_case import BaseTestCase


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
        user = self.User("name")
        user.tokens.append(self.Token(user))
        try:
            self.session.add(user)
            self.session.flush()
            self.assertEqual(len(user.tokens), 1)
            self.assertEqual(user.tokens[0].user, user)
        finally:
                self.session.delete(user)


if __name__ == '__main__':
    unittest.main()
