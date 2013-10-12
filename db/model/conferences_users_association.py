#!/usr/bin/env python
from db.backend import Backend
from sqlalchemy import Column, Integer, Table, ForeignKey

"""
Many to Many association between Conferences and Users.
"""

conferences_users_association = Table(
    'association', Backend.instance().get_base().metadata,
    Column('conference_id', Integer, ForeignKey('conferences.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)
