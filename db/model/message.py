from db.backend import Backend
from sqlalchemy import Column, Integer, String, DateTime
from db import autoupdate
import datetime

class Message(Backend.instance().get_base()):

    """
    Message abstract base model
    """

    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)
    created_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self):
        #make class abstract
        raise TypeError("Message object is an abstract class. It can't be created")

autoupdate.autoupdate()
