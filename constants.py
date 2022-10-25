"""
Constants for 'Create Project structure' 

Created: @marco.mueller.dev@gmail.com

"""
from spaceRoles import RolesManagedSpace, RolesSharedSpace
"""
Tenant
"""
BASE_URL = 'https://{tenantid}.eu.qlikcloud.com'
API_KEY = '{api-key}'



"""
Definition Spacenames
"""
PROJECT_PREFIX                  = 'CUSTOMER'
PROJECT_NAME                    = 'PROJEKT1'
PROJECT_SUB_NAME                = 'GRP'
PROJECT_DEV_SUFFIX              = 'DEV'
PROJECT_TEST_SUFFIX               = 'TEST'
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
ROL_DEV_ADMINISTRATOR    = [RolesSharedSpace.CAN_MANAGE.value]
ROL_DEV_DEVELOPER        = [RolesSharedSpace.CAN_EDIT.value]
ROL_DEV_USER             = []

ROL_TEST_ADMINISTRATOR    = [RolesSharedSpace.CAN_MANAGE.value]
ROL_TEST_DEVELOPER        = [RolesSharedSpace.CAN_EDIT.value]
ROL_TEST_USER             = [RolesManagedSpace.CAN_VIEW.value]

ROL_PROD_ADMINISTRATOR   = [RolesManagedSpace.CAN_MANAGE.value]
ROL_PROD_DEVELOPER       = [RolesManagedSpace.CAN_VIEW.value, RolesManagedSpace.CAN_PUBLISH.value]
ROL_PROD_USER            = [RolesManagedSpace.CAN_CONTRIBUTE.value]

ROL_MANAGED_DATA_ADMINISTRATOR = []
