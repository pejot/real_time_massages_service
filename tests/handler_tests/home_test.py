import unittest, os, os.path, sys
from tornado.testing import AsyncHTTPTestCase
 
# add application root to sys.path
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
sys.path.append(os.path.join(APP_ROOT))

import server

class HomeTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return server.get_app()

    def test_home(self):
        response = self.fetch('/')
        assert "Real-Time REST Messages Service" in response.body, "The Service description is Expected"

if __name__ == '__main__':
    unittest.main()