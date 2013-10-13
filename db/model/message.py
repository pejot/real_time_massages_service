from db.backend import Backend
from db import autoupdate
from sqlalchemy import Column, Integer, String, DateTime
import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Message(Backend.instance().get_base()):

    """
    Message abstract base model.
    """

    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String, nullable=False)
    #message_metadatas = relationship("MessageMetadata", backref="message")
    created_date = Column(
        DateTime, nullable=False, default=datetime.datetime.utcnow)
    
    type = Column(String, nullable=False)
    __mapper_args__ = {
        'polymorphic_on':type,
    }


    def __init__(self):
        # make class abstract
        raise TypeError(
            "Message object is an abstract class. It can't be created")

autoupdate.autoupdate()
