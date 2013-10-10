#!/usr/bin/env python
from tests.base_test import BaseTest
import os
import sys
from tornado.testing import AsyncHTTPTestCase

# add application root to sys.path
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))

from server import Server

class BaseAsyncTestCase(BaseTest, AsyncHTTPTestCase):

    """
    Base test for all handlers tests
    """

    def get_app(self):
        return Server.get_app()
