from db.backend import Backend
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import autoupdate


class User(Backend.instance().get_base()):

    """
    Fake user model
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tokens = relationship("Token", backref="user")

    def __init__(self, name):
        self.name = name

autoupdate.autoupdate()
