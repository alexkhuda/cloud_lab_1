from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:

    app.register_blueprint(err_handler_bp)

    from .orders.bookings_route import bookings_bp
    from .orders.booking_requests_route import booking_requests_bp
    from .orders.payments_route import payments_bp
    from .orders.promotions_route import promotions_bp
    from .orders.properties_address_route import properties_address_bp
    from .orders.properties_route import properties_bp
    from .orders.property_photos_route import property_photos_bp
    from .orders.reviews_route import reviews_bp
    from .orders.transactions_route import transactions_bp
    from .orders.users_route import users_bp

    app.register_blueprint(bookings_bp)
    app.register_blueprint(booking_requests_bp)
    app.register_blueprint(payments_bp)
    app.register_blueprint(promotions_bp)
    app.register_blueprint(properties_address_bp)
    app.register_blueprint(properties_bp)
    app.register_blueprint(property_photos_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(transactions_bp)
    app.register_blueprint(users_bp)
    