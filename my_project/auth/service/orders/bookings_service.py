from my_project.auth.dao import bookings_dao
from my_project.auth.service.general_service import GeneralService


class BookingsService(GeneralService):

    _dao = bookings_dao