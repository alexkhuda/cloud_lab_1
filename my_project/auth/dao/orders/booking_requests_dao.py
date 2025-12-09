from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import BookingRequests


class BookingRequestsDAO(GeneralDAO):
    _domain_type = BookingRequests
