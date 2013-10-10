#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from app_test.base_test_case import BaseTestCase
from tornado.testing import AsyncHTTPTestCase


from server import Server


class BaseAsyncTestCase(BaseTestCase, AsyncHTTPTestCase):

    """
    Base test for all handlers tests.
    """

    def get_app(self):
        return Server.get_app()
