#!/usr/bin/env python
from db.backend import Backend
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from db import autoupdate


class Conference(Backend.instance().get_base()):

    """
    Conference model.
    """

    __tablename__ = 'conferences'

    id = Column(Integer, primary_key=True, autoincrement=True)
    messages = relationship("ConferenceMessage", backref="conference")

autoupdate.autoupdate()
