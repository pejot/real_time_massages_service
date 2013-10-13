#!/usr/bin/env python
import unittest
import os
import sys
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from message_base_test import MessageBaseTestCase


class ConferencesUsersMessagesTest(MessageBaseTestCase):

    @classmethod
    def setUpClass(self):
        super(ConferencesUsersMessagesTest, self).setUpClass()
        from db.model.conference import Conference as ConferenceClass
        from db.model.conference_message import ConferenceMessage as ConferenceMessageClass
        self.Conference = ConferenceClass
        self.ConferenceMessage = ConferenceMessageClass

    def setUp(self):
        super(ConferencesUsersMessagesTest, self).setUp()
        self.user_3 = self.User("name_3")
        self.session.add(self.user_3)
        self.session.flush()

    def tearDown(self):
        self.session.delete(self.user_3)
        super(ConferencesUsersMessagesTest, self).tearDown()

    def test_messages_broadcasting(self):
        conference = self.Conference()
        self.session.add(conference)
        self.session.commit()
        try:
            conference.participants.append(self.user_1)
            conference.participants.append(self.user_2)
            conference.participants.append(self.user_3)
            self.assertEqual(3, len(conference.participants))
            conference.messages.append(
                self.ConferenceMessage("content", self.user_1, conference))
            self.session.commit()
            self.assertEqual(1, len(conference.messages))
            self.assertEqual(1, len(self.user_1.sent_messages))
            self.assertEqual(0, len(self.user_2.sent_messages))
            self.assertEqual(0, len(self.user_3.sent_messages))
            self.assertEqual(0, len(self.user_1.messages_metadatas))
            self.assertEqual(1, len(self.user_2.messages_metadatas))
            self.assertEqual(1, len(self.user_3.messages_metadatas))
            conference.messages.append(
                self.ConferenceMessage("content", self.user_2, conference))
            self.session.commit()
            self.assertEqual(2, len(conference.messages))
            self.assertEqual(1, len(self.user_1.sent_messages))
            self.assertEqual(1, len(self.user_2.sent_messages))
            self.assertEqual(0, len(self.user_3.sent_messages))
            self.assertEqual(1, len(self.user_1.messages_metadatas))
            self.assertEqual(1, len(self.user_2.messages_metadatas))
            self.assertEqual(2, len(self.user_3.messages_metadatas))
            conference.messages.append(
                self.ConferenceMessage("content", self.user_3, conference))
            self.session.commit()
            self.assertEqual(3, len(conference.messages))
            self.assertEqual(1, len(self.user_1.sent_messages))
            self.assertEqual(1, len(self.user_2.sent_messages))
            self.assertEqual(1, len(self.user_3.sent_messages))
            self.assertEqual(2, len(self.user_2.messages_metadatas))
            self.assertEqual(2, len(self.user_2.messages_metadatas))
            self.assertEqual(2, len(self.user_3.messages_metadatas))
        finally:
            self.session.delete(conference)


if __name__ == '__main__':
    unittest.main()
