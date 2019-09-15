from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .artist import Artist
from .user import User
