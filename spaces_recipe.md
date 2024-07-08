As a User I can organise my Spaces
I want to keep List of Spaces


# 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| space               | name, street, city, property_type, maximum_capacity, number_of_bedrooms, number_of bathrooms, price_per_night |

Name of the table (always plural): `spaces`

Column names: `name`, `street`, `city`, `property_type`, `maximum_capacity`, `number_of_bedrooms`, `number_of bathrooms`, `price_per_night` 

Column_types: 
id: SERIAL,
name: text,
street: text,
city: text,
property_type: text,
maximum_capacity: int,
number_of_bedrooms: int,
number_of_bathrooms:int,
price_per_night: numeric

```sql
--file: spaces_table.sql
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
)
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < spaces_table.sql
```