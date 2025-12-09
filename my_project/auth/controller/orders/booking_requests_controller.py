from my_project.auth.service import booking_requests_service
from my_project.auth.controller.general_controller import GeneralController


class BookingRequestsController(GeneralController):

    _service = booking_requests_service
