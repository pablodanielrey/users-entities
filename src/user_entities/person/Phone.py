from enum import Enum
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, func, or_, ForeignKey, Enum as SQLEnum

from user_entities import Base

class PhoneTypes(Enum):
    CELLPHONE = 'CELLPHONE'
    LANDLINE = 'LANDLINE'


class Phone(Base):

    __tablename__ = 'phones'
    
    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)

    number = Column(String)
    type = Column(SQLEnum(PhoneTypes))
    person_id = Column(String, ForeignKey('persons.id'))
