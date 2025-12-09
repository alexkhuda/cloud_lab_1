from my_project.auth.dao import promotions_dao
from my_project.auth.service.general_service import GeneralService


class PromotionsService(GeneralService):

    _dao = promotions_dao