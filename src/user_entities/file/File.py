
from enum import Enum
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, func, or_, ForeignKey, Enum as SQLEnum

from user_entities import Base


class File(Base):

    __tablename__ = 'files'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)

    mimetype = Column(String)
    content = Column(String)
   