from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .artist import Artist
from .albums import Album
from .user import User
