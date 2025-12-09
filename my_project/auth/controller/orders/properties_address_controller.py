from my_project.auth.service import properties_address_service
from my_project.auth.controller.general_controller import GeneralController


class PropertiesAddressController(GeneralController):

    _service = properties_address_service
