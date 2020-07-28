from enum import Enum
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, func, or_, ForeignKey, Enum as SQLEnum

from user_entities import Base

class DegreeTypes(Enum):
    ELEMENTARY = 'ELEMENTARY'
    HIGHER = 'HIGHER'
    COLLEGE = 'COLLEGE'
    MASTER = 'MASTER'
    DOCTORAL = 'DOCTORAL'


class Degree(Base):

    __tablename__ = 'degree'

    type = Column(SQLEnum(DegreeTypes))
    title = Column(String)
    start = Column(DateTime)

    person_id = Column(String, ForeignKey('persons.id'))

    file_id = Column(String, ForeignKey('files.id'))
    file = relationship('File')
