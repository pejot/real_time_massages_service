from db.backend import Backend
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import autoupdate
from conferences_users_association import conferences_users_association

class User(Backend.instance().get_base()):

    """
    Fake user model.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    tokens = relationship("Token", backref="user")
    conferences = relationship("Conference",
                               secondary=conferences_users_association,
                               backref="participants")
    #metadat of messages which should be deliver to user
    messages_metadatas = relationship("MessageMetadata",  backref="receiver")
    #messages which were sent by user
    sent_messages = relationship("Message", backref="sender")

    def __init__(self, name):
        if name is None:
            raise ValueError("Name can't be none")
        if not name.strip():
            raise ValueError("Name can't be empty")
        self.name = name


autoupdate.autoupdate()
