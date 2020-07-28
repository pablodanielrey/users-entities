from enum import Enum


class UserEventTypes(Enum):
    CREATED = 'CREATED'
    UPDATED = 'UPDATED'
    DELETED = 'DELETED'

#class UserEvent(Record):
#    """ Evento para pulsar """
#    type_ = PString()
#    user = PString()
    

