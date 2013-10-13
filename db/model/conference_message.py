#!/usr/bin/env python
from sqlalchemy import Column, Integer
from db import autoupdate
from message import Message
from message_metadata import MessageMetadata
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class ConferenceMessage(Message):

    """
    Confrence Message model.
    """

    __tablename__ = 'conference_messages'
    __mapper_args__ = {
        'polymorphic_identity': 'conference_message',
    }

    id = Column(Integer, ForeignKey('messages.id'), primary_key=True)
    conference_id = Column(Integer, ForeignKey('conferences.id'))
    message_metadatas = relationship("MessageMetadata")

    def __init__(self, content, sender, conference):
        if content is None:
            raise ValueError("Given content is None")
        if not content.strip():
            raise ValueError("Given content is empty")
        if sender is None:
            raise ValueError("Given sender is None")
        if conference is None:
            raise ValueError("Given conference is None")
        self.content = content
        self.sender_id = sender.id
        self.conference_id = conference.id
        for participant in conference.participants:
            if participant is not sender:
                self.message_metadatas.append(
                    MessageMetadata(participant, self))

autoupdate.autoupdate()
