from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Bookings


class BookingsDAO(GeneralDAO):
    _domain_type = Bookings
