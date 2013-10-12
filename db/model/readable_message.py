from sqlalchemy import Column, Integer, Boolean
from db import autoupdate
from sqlalchemy import ForeignKey
from message import Message

class ReadableMessage(Message):

    """
    Readable Message model.
    """

    __tablename__ = 'readable_messages'

    id = Column(Integer, ForeignKey('messages.id'), primary_key=True)
    delivered = Column(Boolean, default=False)
    read = Column(Boolean, default=False)

    def __init__(self):
        # make class abstract
        raise TypeError(
            "Message object is an abstract class. It can't be created")

autoupdate.autoupdate()
