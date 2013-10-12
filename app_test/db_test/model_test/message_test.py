#!/usr/bin/env python
import unittest
import os
import sys
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from app_test.base_test_case import BaseTestCase


class MessageTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(MessageTestCase, self).setUpClass()
        from db.model.message import Message
        self.Message = Message

    def test_abstract_nature(self):
        """Should be created as an abstract class."""
        self.assertRaises(TypeError, self.Message)

if __name__ == '__main__':
    unittest.main()
