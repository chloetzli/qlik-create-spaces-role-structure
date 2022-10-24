from spaceRoles import RolesManagedSpace, RolesSharedSpace
"""
Tenant
"""
BASE_URL = 'https://{your tenant id}.eu.qlikcloud.com'
API_KEY = '{your tenant api key}'


"""
Definition Spacenames
"""
PROJECT_PREFIX                  = 'CUSTOMER'
PROJECT_NAME                    = 'PROJEKT1'
PROJECT_SUB_NAME                = 'GRP'
PROJECT_DEV_SUFFIX              = 'DEV'
PROJECT_QA_SUFFIX               = 'TEST'
PROJECT_DATACONNECTION_SUFFIX   = 'DATA'
PROJECT_DELIMITER               = '_'
NUMBER_OF_SUB                   = 3

"""
AD-Groups
"""
GRP_PROJECT_ADMINISTRATOR   = 'Project 1 admin'
GRP_PROJECT_DEVELOPER       = 'Project 1 developer'
GRP_PROJECT_USER            = 'Project 1 user'

"""
Group, Roles Mapping
"""
ROL_SHARED_ADMINISTRATOR    = [RolesSharedSpace.CAN_MANAGE.value]
ROL_SHARED_DEVELOPER        = [RolesSharedSpace.CAN_EDIT.value]
ROL_SHARED_USER             = []

ROL_MANAGED_ADMINISTRATOR   = [RolesManagedSpace.CAN_MANAGE.value]
ROL_MANAGED_DEVELOPER       = [RolesManagedSpace.CAN_VIEW.value, RolesManagedSpace.CAN_PUBLISH.value]
ROL_MANAGED_USER            = [RolesManagedSpace.CAN_CONTRIBUTE.value]

ROL_MANAGED_DATA_ADMINISTRATOR = [RolesManagedSpace.CAN_MANAGE.value]
