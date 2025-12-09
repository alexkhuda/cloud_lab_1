from .orders.booking_requests_service import BookingRequestsService
from .orders.bookings_service import BookingsService
from .orders.payments_service import PaymentsService
from .orders.promotions_service import PromotionsService
from .orders.properties_address_service import PropertiesAddressService
from .orders.properties_service import PropertiesService
from .orders.property_photos_service import PropertyPhotosService
from .orders.reviews_service import ReviewsService
from .orders.transactions_service import TransactionsService
from .orders.users_service import UsersService

booking_requests_service = BookingRequestsService()
bookings_service = BookingsService()
payments_service = PaymentsService()
promotions_service = PromotionsService()
properties_address_service = PropertiesAddressService()
properties_service = PropertiesService()
property_photos_service = PropertyPhotosService()
reviews_service = ReviewsService()
transactions_service = TransactionsService()
users_service = UsersService()
