from db.backend import Backend
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import autoupdate

class User(Backend.instance().get_base()):

    """
    Fake user model
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    tokens = relationship("Token", backref="user")

    def __init__(self, name):
        if name is None:
            raise ValueError("Name can't be none")
        if not name.strip():
            raise ValueError("Name can't be empty")
        self.name = name

autoupdate.autoupdate()
