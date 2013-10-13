#!/usr/bin/env python
import unittest
import os
import sys
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from message_base_test import MessageBaseTestCase


class ConferenceMessageTestCase(MessageBaseTestCase):

    @classmethod
    def setUpClass(self):
        super(ConferenceMessageTestCase, self).setUpClass()
        from db.model.conference_message import ConferenceMessage
        from db.model.conference import Conference
        self.ConferenceMessage = ConferenceMessage
        self.Conference = Conference

    def setUp(self):
        super(ConferenceMessageTestCase, self).setUp()
        self.conference = self.Conference()
        self.session.add(self.conference)
        self.session.flush()

    def tearDown(self):
        self.session.delete(self.conference)
        super(ConferenceMessageTestCase, self).setUp()

    def test_constructor(self):
        "Should properly store constructor parameters."
        conference_message = self.ConferenceMessage(
            self.content, self.user_1, self.conference)
        self.conference.messages.append(conference_message)
        self.session.flush()
        self.assertEqual(conference_message.content, self.content)
        self.assertEqual(conference_message.sender, self.user_1)
        self.assertEqual(conference_message.conference, self.conference)
        self.assertIsNotNone(conference_message.created_date)

    def test_constructor_with_none_paramters(self):
        "Shouldn't allow to create object with None paramters."
        self.assertRaises(
            ValueError, self.ConferenceMessage, "content", self.User("name"), None)
        self.assertRaises(
            ValueError, self.ConferenceMessage, "", self.User("name"), self.User("name2"))
        self.assertRaises(
            ValueError, self.ConferenceMessage, "content", None, self.User("name"))


if __name__ == '__main__':
    unittest.main()
