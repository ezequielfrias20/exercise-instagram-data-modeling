import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name= Column(String(20) , nullable=False)
    email = Column(String, nullable=False)
    user_name = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)

    posts = relationship("Post",backref="user")
    comments = relationship("Comment",backref="user")
    comment_likes = relationship("CommentLike",backref="user")
    post_likes = relationship("PostLike",backref="user")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    image_url = Column(String(300), nullable=False)
    date_published = Column(DateTime, nullable=False)
    content = Column(String(300))
    latitude = Column(String(8))
    longitude = Column(String(8))
    user_id = Column(Integer, ForeignKey('user.id'))

    comments = relationship("Comment", backref = "post")
    likes = relationship("PostLike", backref = "post")

class PostLike(Base):
    __tablename__ = 'post_like'
    id = Column(Integer, primary_key=True) 
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    
    

class Comment(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    content = Column(String(300), nullable=False)
    date_published = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    likes = relationship("ComentLike", backref = "comment")

class CommentLike(Base):
    __tablename__ = 'comment_like'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment_id = Column(Integer, ForeignKey('comment.id'))

    def to_dict(self):
        return {}


    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')