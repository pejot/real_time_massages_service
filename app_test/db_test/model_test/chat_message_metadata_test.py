#!/usr/bin/env python
import unittest
import os
import sys
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from message_base_test import MessageBaseTestCase

class ChatMessageMetadataTestCase(MessageBaseTestCase):

    @classmethod
    def setUpClass(self):
        super(ChatMessageMetadataTestCase, self).setUpClass()
        from db.model.chat_message_metadata import ChatMessageMetadata
        self.ChatMessageMetadata = ChatMessageMetadata

    def test_constructor(self):
        "Should properly store constructor parameters."
        chat_message_metadata = self.ChatMessageMetadata(self.user_1)
        self.assertEqual(chat_message_metadata.receiver_id, self.user_1.id)

    def test_constructor_with_none_paramters(self):
        "Shouldn't allow to create object with None paramters."
        self.assertRaises(
            ValueError, self.ChatMessageMetadata, None)

if __name__ == '__main__':
    unittest.main()
