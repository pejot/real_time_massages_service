#!/usr/bin/env python
from message_metadata import MessageMetadata
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey
from db import autoupdate

class ChatMessageMetadata(MessageMetadata):

    """
    Chat Message Metadata concrete model.
    """

    __tablename__ = 'chat_message_metadatas'
    __mapper_args__ = {
        'polymorphic_identity':'chat_message_metadata',
    }

    id = Column(Integer, ForeignKey(
        'message_metadatas.id'), primary_key=True)
    chat_message = relationship("ChatMessage", uselist=False, backref="chat_message_metadata")

    def __init__(self, receiver):
        if receiver is None:
            raise ValueError("Given receiver is None")
        self.receiver_id = receiver.id


autoupdate.autoupdate()
