create database automation_test_db;
use automation_test_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(100),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    company VARCHAR(150),
    address_1 VARCHAR(255),
    address_2 VARCHAR(255),
    address_3 VARCHAR(255),
    country VARCHAR(100),
    state VARCHAR(100),
    city VARCHAR(100),
    zip_code VARCHAR(10),
    mobile_number VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE cart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_name VARCHAR(100),
    quantity INT
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    total_amount DECIMAL(10,2)
);

use automation_test_db;
select * from users;
DESCRIBE users;
