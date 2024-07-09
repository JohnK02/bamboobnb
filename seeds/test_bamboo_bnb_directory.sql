DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    password text,
    email text
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    street text,
    city text,
    property_type text,
    maximum_capacity int,
    number_of_bedrooms int,
    number_of_bathrooms int,
    price_per_night numeric(9,2),
    user_id int,
    constraint fk_user foreign key(user_id) references users(id)
);

INSERT INTO users (username, password, email) VALUES ('user1', 'password1', 'email1@email.com');
INSERT INTO users (username, password, email) VALUES ('user2', 'password2', 'email2@email.com');
INSERT INTO users (username, password, email) VALUES ('user3', 'password3', 'email3@email.com');

INSERT INTO spaces (
    name,
    street,
    city,
    property_type,
    maximum_capacity,
    number_of_bedrooms,
    number_of_bathrooms,
    price_per_night,
    user_id
) VALUES (
    'space1',
    'street1',
    'city1',
    'type1',
    1,
    1,
    1,
    100.00,
    1
);
INSERT INTO spaces (
    name,
    street,
    city,
    property_type,
    maximum_capacity,
    number_of_bedrooms,
    number_of_bathrooms,
    price_per_night,
    user_id
) VALUES (
    'space2',
    'street2',
    'city2',
    'type2',
    2,
    2,
    2,
    200.00,
    2
);
INSERT INTO spaces (
    name,
    street,
    city,
    property_type,
    maximum_capacity,
    number_of_bedrooms,
    number_of_bathrooms,
    price_per_night,
    user_id
) VALUES (
    'space3',
    'street3',
    'city3',
    'type3',
    3,
    3,
    3,
    300.00,
    3
);