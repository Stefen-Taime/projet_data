CREATE TABLE customers (
  id SERIAL,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE orders (
    id SERIAL,
    customer_id INTEGER,
    item VARCHAR(255),
    price REAL,
    PRIMARY KEY(id)
);

INSERT INTO customers (first_name, last_name, email)
VALUES('First','Last','first.last@gmail.com');

INSERT INTO customers (first_name, last_name, email)
VALUES('John', 'Doe','jdoe@gmail.com');

INSERT INTO customers (first_name, last_name, email)
VALUES('Jacob', 'Drew', 'jdrew@gmail.com');

UPDATE customers SET first_name = 'Nancy' WHERE id = '3';

INSERT INTO orders (customer_id, item, price)
VALUES (1, 'Sonic Screwdriver', 1000.00);

INSERT INTO orders (customer_id, item, price)
VALUES (2, 'High Quality Broomstick', 40.00);

INSERT INTO orders (customer_id, item, price)
VALUES (1, 'TARDIS', 1000000.00);