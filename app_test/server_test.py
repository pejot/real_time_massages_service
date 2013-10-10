#!/usr/bin/env python
from base_test_case import BaseTestCase
import unittest
from server import Server


class ServerTestCase(BaseTestCase):

    def test_server_get_app(self):
        """Should set backend and tornado application"""
        app = Server.get_app()
        assert app is not None, "Tornado web bapp was expected"

if __name__ == '__main__':
    unittest.main()
