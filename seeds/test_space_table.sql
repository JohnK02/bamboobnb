DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

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
    price_per_night numeric
);