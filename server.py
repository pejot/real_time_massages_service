#!/usr/bin/env python
"""
Start module of simple REST messages service
"""

__version__ = "0.0.1"
__author__ = "@pejot"

import logging
import tornado
import tornado.web
from tornado.options import options, parse_config_file, define
from handlers.home import HomeHandler

define("port", default=8888, type=int)
define("db", default=":memory:")


class Server:

    @classmethod
    def get_app(self):
        return tornado.web.Application(
            [
                (r"/", HomeHandler),
            ],
        )


def main():
    parse_config_file("application.cfg")
    logging.info("Starting tornado server")
    Server.get_app().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
