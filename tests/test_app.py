from flask import app
from playwright.sync_api import Page, expect
from lib.spaces_repository import SpaceRepository
from lib.database_connection import get_flask_database_connection
from lib.users_repository import UsersRepository
from lib.users import Users
from lib.space import Space

# Tests for your routes go here

"""
/POST albums
When I add a new user through POST /users
The user now shows with GET /users
"""

def test_post_users(db_connection, web_client):
    db_connection.seed("seeds/test_bamboo_bnb_directory.sql")
    post_response = web_client.post('/users', data={
        'username': 'user4',
        'password': 'password4',
        'email': 'email4@email.com'
        })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

def test_post_spaces(db_connection, web_client):
    db_connection.seed("seeds/test_bamboo_bnb_directory.sql")
    post_response = web_client.post('/spaces', data={
        'name' : "space1",
        'street': "street1",
        'city': "city1",
        'property_type' : "type1",
        'maximum_capacity' : 1,
        'number_of_bedrooms' : 1,
        'number_of_bathrooms' : 1,
        'price_per_night': 100.00,
        'user_id': 1

        })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == "1, space1, street1, city1, type1, 1, 1, 1, 100.00, 1\n" \
    "2, space2, street2, city2, type2, 2, 2, 2, 200.00, 2\n" \
    "3, space3, street3, city3, type3, 3, 3, 3, 300.00, 3\n" \
    "4, space1, street1, city1, type1, 1, 1, 1, 100.00, 1"

def test_get_spaces(db_connection, web_client):
    db_connection.seed("seeds/test_bamboo_bnb_directory.sql")
    repository = SpaceRepository(db_connection)
    assert repository.all() == [
        Space(1, 'space1', 'street1', 'city1', 'type1', 1, 1, 1, 100.00, 1),
        Space(2, 'space2', 'street2', 'city2', 'type2', 2, 2, 2, 200.00, 2),
        Space(3, 'space3', 'street3', 'city3', 'type3', 3, 3, 3, 300.00, 3),
    ]

def test_delete_spaces(db_connection, web_client):
    db_connection.seed("seeds/test_bamboo_bnb_directory.sql")
    delete_response = web_client.delete('/spaces', data={
        'name' : "space1",
        'street': "street1",
        'city': "city1",
        'property_type' : "type1",
        'maximum_capacity' : 1,
        'number_of_bedrooms' : 1,
        'number_of_bathrooms' : 1,
        'price_per_night': 100.00,
        'user_id': 1
    })
    assert delete_response.status_code == 200