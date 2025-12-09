from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Promotions


class PromotionsDAO(GeneralDAO):
    _domain_type = Promotions
