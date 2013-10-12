from sqlalchemy import Column, Integer
from db import autoupdate
from readable_message import ReadableMessage
from sqlalchemy import ForeignKey

class ChatMessage(ReadableMessage):

    """
    Chat Message model.
    """

    __tablename__ = 'chat_messages'

    id = Column(Integer, ForeignKey('readable_messages.id'), primary_key=True)
    receiver_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, content, sender, receiver):
        if content is None:
            raise ValueError("Given content is None")
        if not content.strip():
            raise ValueError("Given content is empty")
        if sender is None:
            raise ValueError("Given sender is None")
        if receiver is None:
            raise ValueError("Given receiver is None")
        # can be migrated to model constraint field
        if receiver == sender:
            raise ValueError("Receiver and sender must be different")
        self.content = content
        self.sender_id = sender.id
        self.receiver_id = receiver.id


autoupdate.autoupdate()
