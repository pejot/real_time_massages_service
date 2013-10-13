#!/usr/bin/env python
import os
from tornado.options import parse_config_file, define, options
import unittest
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(APP_ROOT))
from db.backend import Backend


class BaseTestCase(unittest.TestCase):

    """
    Base test for all test - loads all configurations and adds app to sys path
    """
    @classmethod
    def setUpClass(self):
        if "port" not in options:
            define("port", default=8888, type=int)
        if "db" not in options:
            define("db", default=":memory:")
        if "db_echo" not in options:
            define("db_echo", default=True)
        config_file = os.path.join(os.path.dirname(__file__), "test.cfg")
        parse_config_file(config_file)
        models_init()

    def setUp(self):
        sessionmaker = Backend.instance().get_sessionmaker()
        self.session = sessionmaker()

    def tearDown(self):
        self.session.close()


def models_init():
    from db.model.conference import Conference
    from db.model.user import User
    from db.model.token import Token
    from db.model.message import Message
    from db.model.message_metadata import MessageMetadata
    from db.model.chat_message import ChatMessage
    from db.model.conference_message import ConferenceMessage

