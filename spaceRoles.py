from enum import Enum

class RolesSharedSpace(Enum):
    CAN_VIEW            = 'consumer' #Kann anzeigen
    CAN_EDIT            = 'producer' #Kann bearbeiten
    CAN_MANAGE          = 'facilitator' #Kann verwalten
    CAN_CONSUME_DATA    = 'dataconsumer' #Kann Daten nutzen

class RolesManagedSpace(Enum):
    CAN_VIEW            = "consumer" #Kann anzeigen
    CAN_CONTRIBUTE      = "contributor" #Kann beitragen
    CAN_CONSUME_DATA    = "dataconsumer" #Kann Daten nutzen
    CAN_MANAGE          = "facilitator" #Kann verwalten
    CAN_PUBLISH         = "publisher" #Kann veröffentlichen