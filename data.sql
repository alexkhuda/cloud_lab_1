USE db_1;

INSERT INTO users (type, first_name, last_name, email, password_hash, phone_number, created_at)
VALUES
('Owner', 'John', 'Doe', 'john@example.com', 'hashed_pass_1', '1234567890', NOW()),
('Tenant', 'Jane', 'Smith', 'jane@example.com', 'hashed_pass_2', '1234567891', NOW()),
('Owner', 'Alice', 'Brown', 'alice@example.com', 'hashed_pass_3', '1234567892', NOW()),
('Tenant', 'Bob', 'Johnson', 'bob@example.com', 'hashed_pass_4', '1234567893', NOW()),
('Owner', 'Charlie', 'Williams', 'charlie@example.com', 'hashed_pass_5', '1234567894', NOW()),
('Tenant', 'David', 'Miller', 'david@example.com', 'hashed_pass_6', '1234567895', NOW()),
('Owner', 'Emma', 'Davis', 'emma@example.com', 'hashed_pass_7', '1234567896', NOW()),
('Tenant', 'Frank', 'Wilson', 'frank@example.com', 'hashed_pass_8', '1234567897', NOW()),
('Owner', 'Grace', 'Taylor', 'grace@example.com', 'hashed_pass_9', '1234567898', NOW()),
('Tenant', 'Henry', 'Anderson', 'henry@example.com', 'hashed_pass_10', '1234567899', NOW()),
('Owner', 'Ivy', 'Thomas', 'ivy@example.com', 'hashed_pass_11', '1234567800', NOW()),
('Tenant', 'Jack', 'Harris', 'jack@example.com', 'hashed_pass_12', '1234567801', NOW());


INSERT INTO properties_address (address, city, country)
VALUES
('123 Main St', 'New York', 'USA'),
('456 Oak St', 'Los Angeles', 'USA'),
('789 Pine St', 'Chicago', 'USA'),
('321 Maple St', 'Houston', 'USA'),
('654 Elm St', 'San Francisco', 'USA'),
('987 Birch St', 'Boston', 'USA'),
('147 Cedar St', 'Seattle', 'USA'),
('258 Spruce St', 'Denver', 'USA'),
('369 Willow St', 'Miami', 'USA'),
('753 Aspen St', 'Dallas', 'USA'),
('852 Redwood St', 'Phoenix', 'USA'),
('951 Cypress St', 'Las Vegas', 'USA');



INSERT INTO properties (user_id, title, description, address_id, price_per_night, created_at)
VALUES
(1, 'Cozy Apartment', 'A nice place to stay', 1, 100.00, NOW()),
(3, 'Luxury Villa', 'Spacious and comfortable', 2, 250.00, NOW()),
(5, 'Modern Loft', 'Great city view', 3, 180.00, NOW()),
(7, 'Beach House', 'Near the sea', 4, 220.00, NOW()),
(1, 'Mountain Cabin', 'Quiet and peaceful', 5, 150.00, NOW()),
(3, 'Studio Apartment', 'Small but cozy', 6, 90.00, NOW()),
(5, 'Suburban Home', 'Perfect for families', 7, 200.00, NOW()),
(7, 'Penthouse Suite', 'Top floor, best view', 8, 300.00, NOW()),
(9, 'Lake House', 'Serene and peaceful', 9, 180.00, NOW()),
(11, 'Country Cottage', 'Charming rural escape', 10, 160.00, NOW()),
(9, 'Downtown Condo', 'Close to everything', 11, 210.00, NOW()),
(11, 'Ski Chalet', 'Perfect for winter sports', 12, 250.00, NOW());


INSERT INTO promotions (name, discount_percentage, start_date, end_date, created_at)
VALUES
('Winter Sale', 10.00, '2025-01-01', '2025-01-31', NOW()),
('Summer Discount', 15.00, '2025-06-01', '2025-06-30', NOW()),
('Weekend Special', 5.00, '2025-03-01', '2025-03-03', NOW()),
('Holiday Deal', 20.00, '2025-12-20', '2025-12-31', NOW()),
('Spring Offer', 12.00, '2025-04-01', '2025-04-15', NOW()),
('Flash Sale', 8.00, '2025-07-10', '2025-07-15', NOW()),
('Loyalty Bonus', 10.00, '2025-09-01', '2025-09-30', NOW()),
('Last Minute Deal', 18.00, '2025-11-15', '2025-11-20', NOW()),
('Autumn Discount', 14.00, '2025-10-01', '2025-10-31', NOW()),
('Early Bird', 10.00, '2025-02-01', '2025-02-28', NOW()),
('Black Friday Deal', 25.00, '2025-11-29', '2025-11-30', NOW()),
('Cyber Monday Special', 20.00, '2025-12-02', '2025-12-03', NOW());


INSERT INTO bookings (property_id, user_id, check_in_date, check_out_date, total_price, date)
VALUES
(1, 2, '2025-01-05', '2025-01-10', 500.00, NOW()),
(2, 4, '2025-02-15', '2025-02-20', 1250.00, NOW()),
(3, 6, '2025-03-10', '2025-03-15', 900.00, NOW()),
(4, 8, '2025-04-05', '2025-04-10', 1100.00, NOW()),
(5, 2, '2025-05-15', '2025-05-20', 750.00, NOW()),
(6, 4, '2025-06-01', '2025-06-05', 360.00, NOW()),
(7, 6, '2025-07-10', '2025-07-15', 1000.00, NOW()),
(8, 8, '2025-08-20', '2025-08-25', 1500.00, NOW()),
(9, 10, '2025-09-05', '2025-09-10', 900.00, NOW()),
(10, 12, '2025-11-15', '2025-11-20', 800.00, NOW()),
(11, 10, '2025-12-01', '2025-12-05', 840.00, NOW()),
(12, 12, '2026-01-05', '2026-01-10', 1250.00, NOW());


INSERT INTO transactions (booking_id, promotion_id, amount, date)
VALUES
(1, 1, 450.00, NOW()),
(2, 2, 1062.50, NOW()),
(3, 3, 855.00, NOW()),
(4, 4, 880.00, NOW()),
(5, 5, 660.00, NOW()),
(6, 6, 331.20, NOW()),
(7, 7, 900.00, NOW()),
(8, 8, 1230.00, NOW()),
(9, 9, 774.00, NOW()),
(10, 10, 720.00, NOW()),
(11, 11, 630.00, NOW()),
(12, 12, 1000.00, NOW());

INSERT INTO payments (transaction_id, service_fee, owner_amount, date)
VALUES
(1, 30.00, 420.00, NOW()),
(2, 75.00, 987.50, NOW()),
(3, 40.00, 815.00, NOW()),
(4, 50.00, 830.00, NOW()),
(5, 45.00, 615.00, NOW()),
(6, 25.00, 306.20, NOW()),
(7, 55.00, 845.00, NOW()),
(8, 60.00, 1170.00, NOW()),
(9, 40.00, 734.00, NOW()),
(10, 35.00, 685.00, NOW()),
(11, 50.00, 580.00, NOW()),
(12, 60.00, 940.00, NOW());


INSERT INTO reviews (property_id, user_id, rating, comment, created_at)
VALUES
(1, 2, 5, 'Amazing stay!', NOW()),
(2, 4, 4, 'Great location, but noisy.', NOW()),
(3, 6, 5, 'Perfect for vacation.', NOW()),
(4, 8, 3, 'Good, but needs improvement.', NOW()),
(5, 2, 5, 'Loved it!', NOW()),
(6, 4, 4, 'Nice and clean.', NOW()),
(7, 6, 5, 'Highly recommend.', NOW()),
(8, 8, 3, 'Okay experience.', NOW()),
(9, 10, 5, 'Fantastic view!', NOW()),
(10, 12, 4, 'Very cozy and clean.', NOW()),
(11, 10, 5, 'Loved every moment.', NOW()),
(12, 12, 3, 'Good, but pricey.', NOW());


INSERT INTO property_photos (property_id, photo_url, uploaded_at)
VALUES
(1, 'photo1.jpg', NOW()),
(2, 'photo2.jpg', NOW()),
(3, 'photo3.jpg', NOW()),
(4, 'photo4.jpg', NOW()),
(5, 'photo5.jpg', NOW()),
(6, 'photo6.jpg', NOW()),
(7, 'photo7.jpg', NOW()),
(8, 'photo8.jpg', NOW()),
(9, 'photo9.jpg', NOW()),
(10, 'photo10.jpg', NOW()),
(11, 'photo11.jpg', NOW()),
(12, 'photo12.jpg', NOW());


INSERT INTO booking_requests (property_id, user_id, status, date)
VALUES
(1, 2, 'Pending', NOW()),
(2, 4, 'Accepted', NOW()),
(3, 6, 'Rejected', NOW()),
(4, 8, 'Pending', NOW()),
(5, 2, 'Accepted', NOW()),
(6, 4, 'Rejected', NOW()),
(7, 6, 'Pending', NOW()),
(8, 8, 'Accepted', NOW()),
(9, 10, 'Pending', NOW()),
(10, 12, 'Accepted', NOW()),
(11, 10, 'Rejected', NOW()),
(12, 12, 'Pending', NOW());