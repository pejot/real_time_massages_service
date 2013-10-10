from db.backend import Backend
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from db import autoupdate
import uuid

class Token(Backend.instance().get_base()):

    """
    Fake token authentication model
    """

    __tablename__ = 'tokens'

    id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, user):
        if user is None:
            raise TypeError("Given user is None")
        if user.id is None:
            raise TypeError("Given user has None id")
        self.id = str(uuid.uuid1())
        self.user_id = user.id

autoupdate.autoupdate()
