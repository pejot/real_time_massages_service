#!/usr/bin/env python
import unittest
import os
import sys
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from app_test.base_test_case import BaseTestCase


class ChatMessageTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(ChatMessageTestCase, self).setUpClass()
        from db.model.chat_message import ChatMessage
        from db.model.user import User
        self.ChatMessage = ChatMessage
        self.User = User

    def setUp(self):
        super(ChatMessageTestCase, self).setUp()
        from db.model.chat_message import ChatMessage
        from db.model.user import User
        self.ChatMessage = ChatMessage
        self.User = User
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
        super(ChatMessageTestCase, self).tearDown()

    def test_constructor(self):
        "Should properly store constructor parameters."
        chat_message = self.ChatMessage(self.content, self.user_1, self.user_2)
        self.assertEqual(chat_message.content, self.content)

    def test_timestamp(self):
        "Should automatically gives timestamp."
        chat_message = self.ChatMessage(self.content, self.user_1, self.user_2)
        self.session.add(chat_message)
        self.session.flush()
        self.assertIsNotNone(chat_message.created_date)

    def test_constructor_with_none_paramters(self):
        "Shouldn't allow to create object with None paramters."
        self.assertRaises(
            ValueError, self.ChatMessage, "content", self.User("name"), None)
        self.assertRaises(
            ValueError, self.ChatMessage, "", self.User("name"), self.User("name2"))
        self.assertRaises(
            ValueError, self.ChatMessage, "content", None, self.User("name"))

if __name__ == '__main__':
    unittest.main()
