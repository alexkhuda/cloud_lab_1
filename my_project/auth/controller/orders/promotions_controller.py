from my_project.auth.service import promotions_service
from my_project.auth.controller.general_controller import GeneralController


class PromotionsController(GeneralController):

    _service = promotions_service
