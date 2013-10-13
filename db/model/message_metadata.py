from db.backend import Backend
from sqlalchemy import Column, Integer, Boolean
from db import autoupdate
from sqlalchemy import ForeignKey

class MessageMetadata(Backend.instance().get_base()):

    """
    Message Metadata model.
    """

    __tablename__ = 'message_metadatas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    delivered = Column(Boolean, default=False)
    read = Column(Boolean, default=False)
    receiver_id = Column(Integer, ForeignKey('users.id'))
    message_id = Column(Integer, ForeignKey('messages.id')) 

    def __init__(self, receiver, message):
        if receiver is None:
            raise ValueError("Given receiver is None")
        self.receiver_id = receiver.id
        self.message = message


autoupdate.autoupdate()
