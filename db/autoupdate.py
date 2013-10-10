from backend import Backend
from sqlalchemy.orm import scoped_session


def autoupdate():
    """
    Autoupdate data layer about new models in engines.
    """
    scoped_session(Backend.instance().get_sessionmaker)
    Backend.instance().get_base().metadata.create_all(
        Backend.instance().get_engine())
