from my_project.auth.dao import booking_requests_dao
from my_project.auth.service.general_service import GeneralService


class BookingRequestsService(GeneralService):

    _dao = booking_requests_dao