"""
This is a database model file
"""

from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class User(BASE):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __repr__(self):
        return F"{self.name}"
