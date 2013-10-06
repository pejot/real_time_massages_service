#!/usr/bin/env python
import unittest
from base_test import BaseTestCase


class HomeTestCase(BaseTestCase):

    def test_home(self):
        """Should gives a home page - Service Description"""
        response = self.fetch('/')
        assert "Real-Time REST Messages Service" in response.body, "The Service Description was expected"

if __name__ == '__main__':
    unittest.main()
