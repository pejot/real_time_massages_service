#!/usr/bin/env python
import unittest
import os
import sys
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from chat_message_test import ChatMessageTestCase


class ChatMessagesUsersTestCase(ChatMessageTestCase):

    @classmethod
    def setUpClass(self):
        super(ChatMessagesUsersTestCase, self).setUpClass()
        from db.model.user import User
        self.User = User

    def test_messages_property(self):
        "Should give a list of messages."
        chat_message = self.ChatMessage(self.content, self.user_1, self.user_2)
        self.session.add(chat_message)
        self.session.flush()
        self.assertEqual(1, len(self.session.query(self.ChatMessage).all()))
        self.assertEqual(1, len(self.session.query(self.MessageMetadata).all()))
        self.assertEqual(0, len(self.user_1.messages_metadatas))
        self.assertEqual(1, len(self.user_2.messages_metadatas))
        self.assertEqual(1, len(self.user_1.sent_messages))
        self.assertEqual(0, len(self.user_2.sent_messages))

if __name__ == '__main__':
    unittest.main()
