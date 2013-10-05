#!/usr/bin/env python
"""
Start module of simple REST messages service
"""

__version__ = "0.0.1"
__author__ = "@pejot"

import logging
import tornado
import tornado.web
from tornado.options import options, parse_command_line, define
from handlers.home import HomeHandler

define("port", default=8888, help="run on the given port", type=int)


def get_app():
    return tornado.web.Application(
        [
            (r"/", HomeHandler),
        ],
    )


def main():
    parse_command_line()
    app = get_app()
    logging.info("Starting tornado server")
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
