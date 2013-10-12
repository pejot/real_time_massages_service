from db.backend import Backend
from sqlalchemy import Column, Integer
from db import autoupdate


class Conference(Backend.instance().get_base()):

    """
    Conference model
    """

    __tablename__ = 'conferences'

    id = Column(Integer, primary_key=True, autoincrement=True)


autoupdate.autoupdate()
