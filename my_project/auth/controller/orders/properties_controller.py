from my_project.auth.service import properties_service
from my_project.auth.controller.general_controller import GeneralController


class PropertiesController(GeneralController):

    _service = properties_service
