import datetime
from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy import DateTime

"""Define the Artist model"""


class Artist(db.Model, BaseModel, metaclass=MetaBaseModel):
    
    """Artist Model"""
    __tablename__ = "Artist"
    
    fullname = db.Column(db.String(200), primary_key=True)
    artist_handle =  db.Column(db.String(50), primary_key=True)
    dob = db.Column(db.String(30), primary_key=True)
    genre = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(50), primary_key=True, unique=True)
    password = db.Column(db.String(20), primary_key=True)
    date_joined = db.Column(DateTime(), default=datetime.datetime.utcnow)
    donations_total = db.Column(db.String(500))
    follower_count = db.Column(db.Integer, default=0, primary_key=True)
    following_count = db.Column(db.Integer, default=0,primary_key=True)
    # social_media = relationship(social media)
    #supporters = relationship(supporters)
    #followers = relations()
    #following = relationship()
    #songs = relationship(songs)
    #albums = relationship(albums)
    # posts(relationship)

    def __init__(self, fullname, artist_handle, dob, genre, username, password,  donations_total, follower_count, following_count):
        """ Create a new Artist """
        self.fullname = fullname
        self.artist_handle = artist_handle
        self.dob = dob
        self.genre = genre
        self.username = username
        self.password = password
        self.donations_total = donations_total
        self.following_count = following_count
        self.follower_count = following_count

        
        
    