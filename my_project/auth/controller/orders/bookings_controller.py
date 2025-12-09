from my_project.auth.service import bookings_service
from my_project.auth.controller.general_controller import GeneralController


class BookingsController(GeneralController):

    _service = bookings_service
