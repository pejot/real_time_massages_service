#!/usr/bin/env python
from sqlalchemy import Column, Integer
from db import autoupdate
from message import Message
from sqlalchemy import ForeignKey, UniqueConstraint
from message_metadata import MessageMetadata
from sqlalchemy.orm import relationship


class ChatMessage(Message):

    """
    Chat Message model.
    """

    __tablename__ = 'chat_messages'
    __mapper_args__ = {
        'polymorphic_identity': 'chat_message',
    }
    UniqueConstraint('id', 'col3', name='uix_1')
    id = Column(Integer, ForeignKey('messages.id'), primary_key=True)
    message_metadata = relationship("MessageMetadata", uselist=False)

    def __init__(self, content, sender, receiver):
        if content is None:
            raise ValueError("Given content is None")
        if not content.strip():
            raise ValueError("Given content is empty")
        if sender is None:
            raise ValueError("Given sender is None")
        if receiver is None:
            raise ValueError("Given receiver is None")
        # can be migrated to model constraint field
        if receiver == sender:
            raise ValueError("Receiver and sender must be different")
        self.content = content
        self.sender_id = sender.id
        message_metadata = MessageMetadata(receiver, self)
        self.message_metadata = message_metadata


autoupdate.autoupdate()
