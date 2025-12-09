from .orders.booking_requests_dao import BookingRequestsDAO
from .orders.bookings_dao import BookingsDAO
from .orders.payments_dao import PaymentsDAO
from .orders.promotions_dao import PromotionsDAO
from .orders.properties_address_dao import PropertiesAddressDAO
from .orders.properties_dao import PropertiesDAO
from .orders.property_photos_dao import PropertyPhotosDAO
from .orders.reviews_dao import ReviewsDAO
from .orders.transactions_dao import TransactionsDAO
from .orders.users_dao import UsersDAO

booking_requests_dao = BookingRequestsDAO()
bookings_dao = BookingsDAO()
payments_dao = PaymentsDAO()
promotions_dao = PromotionsDAO()
properties_address_dao = PropertiesAddressDAO()
properties_dao = PropertiesDAO()
property_photos_dao = PropertyPhotosDAO()
reviews_dao = ReviewsDAO()
transactions_dao = TransactionsDAO()
users_dao = UsersDAO()
