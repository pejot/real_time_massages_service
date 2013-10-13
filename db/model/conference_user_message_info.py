#!/usr/bin/env python
from sqlalchemy import Column, Integer, UniqueConstraint, ForeignKey
from db import autoupdate
from readable_message import ReadableMessage


class ConferenceUserMessageInfo(ReadableMessage):

    """
    Conference user message info. Provides delivered and read fields.
    """

    __tablename__ = 'conference_user_message_infos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    conference_message_id = Column(
        Integer, ForeignKey('conference_message.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    UniqueConstraint('conference_message_id',
                     'user_id', name='message_info_uniqueness')

autoupdate.autoupdate()
