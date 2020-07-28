
from enum import Enum
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, func, or_, ForeignKey, Enum as SQLEnum

from user_entities import Base



class MailTypes(Enum):
    NOTIFICATION = 'NOTIFICATION'
    INSTITUTIONAL = 'INSTITUTIONAL'
    ALTERNATIVE = 'ALTERNATIVE'


class Mail(Base):

    __tablename__ = 'mails'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)

    type = Column(SQLEnum(MailTypes))
    email = Column(String)
    confirmed = Column(DateTime()) 
    person_id = Column(String, ForeignKey('persons.id'))
    
