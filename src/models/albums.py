import datetime
from . import db
from .abc import BaseModel, MetaBaseModel
from .artist import Artist

"""Define Album Model"""


class Album(db.Model, BaseModel, metaclass=MetaBaseModel):
    "Album Model"
    __tablename__ = "Album"
    artist_id = db.ForeignKey("Artist")
    title = db.Column(db.String(50), primary_key=True)
    album_id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(50), primary_key=True)
    album_release_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    length = db.Column(db.String(50), primary_key=True)
    #songs = relationsips(songs)
    #featuring relationship(artist)
    #produced relationship(artist)

    def __init__(self,title, album_id, genre,length, artist_id=None):
        self.title = title
        self.album_id = album_id
        self.genre = genre
        self.length = length
        self.artist_id = artist_id