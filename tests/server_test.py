#!/usr/bin/env python
import unittest
import os, sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(APP_ROOT))
from server import Server
#Because of the singleton nature of Server - one test case for one unit test

class ServerTestCase(unittest.TestCase):

    def test_server_get_app(self):
        """ Should set backend and tornado application """
        app = Server.get_app()
        assert app is not None, "Tornado web bapp was expected"

if __name__ == '__main__':
    unittest.main()
