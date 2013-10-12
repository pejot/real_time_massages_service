from db.backend import Backend
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from db import autoupdate
import datetime
from sqlalchemy import ForeignKey


class Message(Backend.instance().get_base()):

    """
    Message abstract base model.
    """

    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String, nullable=False)
    created_date = Column(
    DateTime, nullable=False, default=datetime.datetime.utcnow)
    delivered = Column(Boolean, default=False)
    read = Column(Boolean, default=False)

    def __init__(self):
        # make class abstract
        raise TypeError(
            "Message object is an abstract class. It can't be created")

autoupdate.autoupdate()
