from my_project.auth.dao import users_dao
from my_project.auth.service.general_service import GeneralService


class UsersService(GeneralService):

    _dao = users_dao