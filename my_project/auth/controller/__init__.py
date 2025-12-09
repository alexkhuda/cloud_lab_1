from .orders.booking_requests_controller import BookingRequestsController
from .orders.bookings_controller import BookingsController
from .orders.payments_controller import PaymentsController
from .orders.promotions_controller import PromotionsController
from .orders.properties_address_controller import PropertiesAddressController
from .orders.properties_controller import PropertiesController
from .orders.property_photos_controller import PropertyPhotosController
from .orders.reviews_controller import ReviewsController
from .orders.transactions_controller import TransactionsController
from .orders.users_controller import UsersController

booking_requests_controller = BookingRequestsController()
bookings_controller = BookingsController()
payments_controller = PaymentsController()
promotions_controller = PromotionsController()
properties_address_controller = PropertiesAddressController()
properties_controller = PropertiesController()
property_photos_controller = PropertyPhotosController()
reviews_controller = ReviewsController()
transactions_controller = TransactionsController()
users_controller = UsersController()