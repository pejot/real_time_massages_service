#!/usr/bin/env python
import abc


class AbstractBackend:

    """
    The abstract interface of database layer access
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_metadata(self):
        None

    @abc.abstractmethod
    def get_sessionmaker(self):
        None

    @abc.abstractmethod
    def get_engine(self):
        None

    @abc.abstractmethod
    def get_base(self):
        None

    @abc.abstractmethod
    def get_session(self):
        None