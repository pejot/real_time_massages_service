from db.backend import Backend
from sqlalchemy import Column, Integer, Boolean, String
from db import autoupdate
from sqlalchemy import ForeignKey

class MessageMetadata(Backend.instance().get_base()):

    """
    Message Metadata abstract model.
    """

    __tablename__ = 'message_metadatas'

    
    id = Column(Integer, primary_key=True, autoincrement=True)
    delivered = Column(Boolean, default=False)
    read = Column(Boolean, default=False)
    receiver_id = Column(Integer, ForeignKey('users.id'))
    type = Column(String, nullable=False)

    __mapper_args__ = {
        'polymorphic_on':type,
    }

    def __init__(self):
        # make class abstract
        raise TypeError(
            "Message object is an abstract class. It can't be created")


autoupdate.autoupdate()
