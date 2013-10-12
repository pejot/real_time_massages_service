#!/usr/bin/env python
from base_async_test_case import BaseAsyncTestCase
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from app_test.base_test_case import BaseTestCase

class HomeTestCase(BaseAsyncTestCase, BaseTestCase):

    def test_home(self):
        """Should gives a home page - Service Description."""
        response = self.fetch('/')
        assert "Real-Time REST Messages Service" in response.body, "The Service Description was expected"

if __name__ == '__main__':
    unittest.main()
