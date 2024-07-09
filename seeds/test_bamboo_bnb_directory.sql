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
    price_per_night numeric,
    user_id int,
    constraint fk_user foreign key(user_id) references users(id)
);