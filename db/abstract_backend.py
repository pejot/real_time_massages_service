#!/usr/bin/env python
class AbstractBackend:

    """
    The abstract interface of database layer access
    """

    def get_metadata(self):
        raise NotImplementedError("The method not implemented")

    def get_sessionmaker(self):
        raise NotImplementedError("The method not implemented")

    def get_engine(self):
        raise NotImplementedError("The method not implemented")

    def get_base(self):
        raise NotImplementedError("The method not implemented")
