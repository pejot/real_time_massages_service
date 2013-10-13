#!/usr/bin/env python
from db.backend import Backend
from sqlalchemy import Column, Integer, Table, ForeignKey

"""
Many to Many association between Conferences and Users.
"""

conference_messages_users_association = Table(
    'conference_messages_users_association', Backend.instance(
    ).get_base().metadata,
    Column('conference_message_id', Integer, ForeignKey('conferences.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)
