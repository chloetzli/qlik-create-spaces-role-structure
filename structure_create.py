"""
Implementation of the 'Create Project structure' 

Created: @marco.mueller.dev@gmail.com

"""
import logging
from qlik_sdk import AuthType, Config, Spaces, SpaceCreate, AssignmentCreate
from Groups import Groups

import constants


logger = logging.getLogger(__name__)

"""
Creating Spaces according to definitions

"""
def createSpaces(conf, groupIds):
    spaces = Spaces(conf)
    
    a = 0
    while a < constants.NUMBER_OF_SUB:

        """
        Create Shared Spaces for development
        """
        
        space_name_def_dev = [constants.PROJECT_PREFIX, constants.PROJECT_NAME, constants.PROJECT_SUB_NAME, constants.PROJECT_DEV_SUFFIX, str(a)]
        dev_space = spaces.create(SpaceCreate(name='_'.join(space_name_def_dev), type="shared", description=""))
        
        """
        Set Permissions
        """
        dev_space.create_assignment(AssignmentCreate(assigneeId=groupIds.get('grp_project_administrator_id'), roles=constants.ROL_DEV_ADMINISTRATOR, type='group'))
        dev_space.create_assignment(AssignmentCreate(assigneeId=groupIds.get('grp_project_developer_id'), roles=constants.ROL_DEV_DEVELOPER, type='group'))
        if constants.ROL_DEV_USER: dev_space.create_assignment(AssignmentCreate(assigneeId=groupIds.get('grp_project_user_id'), roles=constants.ROL_DEV_USER, type='group'))

        """
        Create Shared Spaces for test
        """
        
        space_name_test = [constants.PROJECT_PREFIX, constants.PROJECT_NAME, constants.PROJECT_SUB_NAME, constants.PROJECT_TEST_SUFFIX, str(a)]
        test_space = spaces.create(SpaceCreate(name='_'.join(space_name_test), type="shared", description=""))
        
        """
        Set Permissions
        """
        test_space.create_assignment(AssignmentCreate(assigneeId=groupIds.get('grp_project_administrator_id'), roles=constants.ROL_TEST_ADMINISTRATOR, type='group'))
        test_space.create_assignment(AssignmentCreate(assigneeId=groupIds.get('grp_project_developer_id'), roles=constants.ROL_TEST_DEVELOPER, type='group'))
        if constants.ROL_TEST_USER: test_space.create_assignment(AssignmentCreate(assigneeId=groupIds.get('grp_project_user_id'), roles=constants.ROL_TEST_USER, type='group'))


        """
        Create Managed Spaces for Endusers
        """

        space_name_def = [constants.PROJECT_PREFIX, constants.PROJECT_NAME, constants.PROJECT_SUB_NAME, str(a)]
        space = spaces.create(SpaceCreate(name='_'.join(space_name_def), type="managed", description=""))
        
        """
        Set Permissions
        """
        space.create_assignment(AssignmentCreate(assigneeId=groupIds.get('grp_project_administrator_id'), roles=constants.ROL_PROD_ADMINISTRATOR, type='group'))
        space.create_assignment(AssignmentCreate(assigneeId=groupIds.get('grp_project_developer_id'), roles=constants.ROL_PROD_DEVELOPER, type='group'))
        space.create_assignment(AssignmentCreate(assigneeId=groupIds.get('grp_project_user_id'), roles=constants.ROL_PROD_USER, type='group'))

        a += 1
    """
    Create Managed Spaces for Dataconnections
    """
    if constants.ROL_MANAGED_DATA_ADMINISTRATOR: 
        space_name_def = [constants.PROJECT_PREFIX, constants.PROJECT_NAME, constants.PROJECT_SUB_NAME, constants.PROJECT_DATACONNECTION_SUFFIX, str(a)]
        space_data = spaces.create(SpaceCreate(name='_'.join(space_name_def), type="managed", description=""))
            
        """
        Set Permissions
        """
        space_data.create_assignment(AssignmentCreate(assigneeId=groupIds.get('grp_project_administrator_id'), roles=constants.ROL_MANAGED_DATA_ADMINISTRATOR, type='group'))




def getGroups(conf) -> dict:
    
    groups = Groups(conf).get_groups()
    groupIds = {}
    
    for group in groups.pagination:
        if group.name==constants.GRP_PROJECT_ADMINISTRATOR:
            groupIds['grp_project_administrator_id'] = group.id
        if group.name==constants.GRP_PROJECT_DEVELOPER:
            groupIds['grp_project_developer_id'] = group.id
        if group.name==constants.GRP_PROJECT_USER:
            groupIds['grp_project_user_id'] = group.id
    
    return groupIds

def run(config) -> None:

    groupIds = getGroups(config)
    createSpaces(config, groupIds)



if __name__ == "__main__":
    """
    Setting Up Config
    """
    conf = Config(host=constants.BASE_URL, auth_type=AuthType.APIKey, api_key=constants.API_KEY)

    
    run(conf)
