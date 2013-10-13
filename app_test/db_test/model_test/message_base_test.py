#!/usr/bin/env python
import unittest
import os
import sys
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from app_test.base_test_case import BaseTestCase


class MessageBaseTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(MessageBaseTestCase, self).setUpClass()
        from db.model.user import User
        self.User = User

    def setUp(self):
        super(MessageBaseTestCase, self).setUp()
        self.user_1 = self.User("name_1")
        self.user_2 = self.User("name_2")
        self.content = "content"
        self.session.add(self.user_1)
        self.session.add(self.user_2)
        self.session.flush()

    def stearDown(self):
        self.session.delete(self.user_1)
        self.session.delete(self.user_2)
        self.session.flush()
        super(MessageBaseTestCase, self).tearDown()

if __name__ == '__main__':
    unittest.main()
