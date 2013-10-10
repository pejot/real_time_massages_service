#!/usr/bin/env python
""" 
Home Handler - Gives the service description
"""

import tornado.web

SERVICE_DESCRIPTION = "This is the Real-Time REST Messages Service. Go to API documentatio for details."


class HomeHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(SERVICE_DESCRIPTION)
