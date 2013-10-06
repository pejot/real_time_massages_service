#!/usr/bin/env python
import os
import sys
from tornado.testing import AsyncHTTPTestCase

# add application root to sys.path
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))

from server import Server
from tornado.options import parse_config_file


class BaseTestCase(AsyncHTTPTestCase):

    """
    Base test for all handlers tests - sets up server and data access layer
    """

    def get_app(self):
        config_file = os.path.join(os.path.dirname(__file__), "test.cfg")
        parse_config_file(config_file)
        return Server.get_app()
