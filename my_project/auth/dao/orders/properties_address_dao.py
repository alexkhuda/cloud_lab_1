from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import PropertiesAddress


class PropertiesAddressDAO(GeneralDAO):
    _domain_type = PropertiesAddress
