from sqlalchemy import Column, Integer
from db import autoupdate
from db.model.message import Message
from sqlalchemy import ForeignKey, CheckConstraint


class ChatMessage(Message):

    """
    Chat Message model
    """

    __tablename__ = 'chat_messages'

    id = Column(Integer, ForeignKey('messages.id'), primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'), CheckConstraint(
        'sender_id != receiver_id', name='check_sender_receiver_uniqueness'))
    
    def __init__(self, content, sender, receiver):
        if content is None:
            raise ValueError("Given content is None")
        if not content.strip():
            raise ValueError("Given content is empty")
        if sender is None:
            raise ValueError("Given sender is None")
        if receiver is None:
            raise ValueError("Given receiver is None")
        self.content = content
        self.sender_id = sender.id
        self.receiver_id = receiver.id


autoupdate.autoupdate()
