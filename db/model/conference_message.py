#!/usr/bin/env python
from sqlalchemy import Column, Integer
from db import autoupdate
from db.model.message import Message
from sqlalchemy import ForeignKey


class ConferenceMessage(Message):

    """
    Confrence Message model.
    """

    __tablename__ = 'conference_messages'

    id = Column(Integer, ForeignKey('messages.id'), primary_key=True)
    conference_id = Column(Integer, ForeignKey('conferences.id'))

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


autoupdate.autoupdate()
