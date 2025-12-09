from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Properties


class PropertiesDAO(GeneralDAO):
    _domain_type = Properties
