#!/usr/bin/env python
import unittest
import os
import sys
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import time
from chat_message_test import ChatMessageTestCase


class ChatMessagesUsersTestCase(ChatMessageTestCase):

    @classmethod
    def setUpClass(self):
        super(ChatMessagesUsersTestCase, self).setUpClass()
        from db.model.chat_message import ChatMessage
        from db.model.user import User
        self.ChatMessage = ChatMessage
        self.User = User

    def stest_messages_property(self):
        "Should give a list of messages."
        chat_message = self.ChatMessage(self.content, self.user_1, self.user_2)
        self.user_1.chat_messages.append(chat_message)
        self.session.flush()
        self.assertEqual(1, len(self.session.query(self.ChatMessage).all()))
        self.assertEqual(1, len(self.user_1.chat_messages))
        self.assertEqual(1, len(self.user_2.chat_messages))
        self.assertEqual(
            1, len(self.session.query(self.User).get(self.user_1.id).chat_messages))
        self.assertEqual(
            1, len(self.session.query(self.User).get(self.user_2.id).chat_messages))

    def test_messages_order_by_property(self):
        "Should give user's messages sorted by timestamp."
        # TODO! make some mess with id and saving orderuser_1 =
        # self.User("name_1")
        chat_message = self.ChatMessage(self.content, self.user_1, self.user_2)
        self.user_1.chat_messages.append(chat_message)
        self.session.flush()
        time.sleep(1)
        chat_message_2 = self.ChatMessage(
            self.content + "_2", self.user_1, self.user_2)
        self.user_1.chat_messages.append(chat_message_2)
        self.assertEqual(2, len(self.user_1.chat_messages))
        self.assertEqual(2, len(self.user_2.chat_messages))

        g_date_1 = self.user_1.chat_messages[1].created_date
        s_date_1 = self.user_1.chat_messages[0].created_date
        g_date_2 = self.user_2.chat_messages[1].created_date
        s_date_2 = self.user_2.chat_messages[0].created_date
        self.assertGreater(g_date_1, s_date_1)
        self.assertGreater(g_date_2, s_date_2)


if __name__ == '__main__':
    unittest.main()
