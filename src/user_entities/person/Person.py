import pytz
import uuid
from enum import Enum
from datetime import datetime, time, timedelta
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, func, or_, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship

from user_entities import Base


class Person(Base):

    __tablename__ = 'persons'
    
    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)

    lastname = Column(String)
    firstname = Column(String)
    gender = Column(String)
    marital_status = Column(String)
    birthplace = Column(String)
    birthdate = Column(DateTime())
    residence = Column(String)
    address = Column(String)
        
    mails = relationship('Mail')
    phones = relationship('Phone')
    identity_numbers = relationship('IdentityNumber')

    """
    def get_birthdate(self, tz):
        return self._localize_date_on_zone(self.birthdate, tz)

    def _localize_date_on_zone(self, date, tz='America/Argentina/Buenos_Aires'):
        if date is None:
            return None
        timezone = pytz.timezone(tz)
        dt = datetime.combine(date, time(0))
        dt = timezone.localize(dt)
        return dt

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    """


class IdentityNumberTypes(Enum):
    DNI = 'DNI'
    LC = 'LC'
    LE = 'LE'
    PASSPORT = 'PASSPORT'
    CUIL = 'CUIL'
    CUIT = 'CUIT'
    STUDENT = 'STUDENT'


class IdentityNumber(Base):

    __tablename__ = 'identity_numbers'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)

    type = Column(SQLEnum(IdentityNumberTypes))
    number = Column(String)
    person_id = Column(String, ForeignKey('persons.id'))
   
    file_id = Column(String, ForeignKey('files.id'))
    file = relationship('File')

