from my_project.auth.dao import properties_dao
from my_project.auth.service.general_service import GeneralService


class PropertiesService(GeneralService):

    _dao = properties_dao