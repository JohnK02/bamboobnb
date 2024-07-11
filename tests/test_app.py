from flask import app
from playwright.sync_api import Page, expect
from lib.spaces_repository import SpaceRepository
from lib.database_connection import get_flask_database_connection
from lib.users_repository import UsersRepository
from lib.user import User
from lib.space import Space

# Tests for your routes go here

# def test_get_login(page, test_web_address):
#     page.goto(f"http://{test_web_address}/login")
#     page.fill('username', 'user1')
#     page.fill('password', 'password1')
#     page.click('submit')
#     assert "", 200

"""
GET /
When I access the homepage
The correct information for the tags shows
"""

def test_get_home(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Spaces")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text([
        "space1",
        "space2",
        "space3"
    ])

"""
GET /registration
When I access the registration page
The correct information for the tags shows
"""
def test_registration(page, test_web_address):
    page.goto(f'http://{test_web_address}/registration')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Registration")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        "Username",
        "Password",
        "Email address",
        "Register",
        ""
    ])

"""
GET /login
When I access the login page
The correct information for the tag shows
"""
def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Login")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        "Username",
        "Password",
        "Login"
    ])

"""
/POST users
When I add a new user through POST /users
The user should appear in the DB
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
    repo = UsersRepository(db_connection)
    result = repo.all()
    assert result == [
        User(1, 'user1', 'password1', 'email1@email.com'),
        User(2, 'user2', 'password2', 'email2@email.com'),
        User(3, 'user3', 'password3', 'email3@email.com'),
        User(4, 'user4', 'password4', 'email4@email.com')
    ]

"""
POST /users
When I access GET /registration
And fill out the form
The user is added to the DB
"""
def test_registration_form(page, test_web_address):
    page.goto(f'http://{test_web_address}/registration')
    page.fill("input[name='username']", "user4")
    page.fill("input[name='password']", "password4")
    page.fill("input[name='email']", "email4@email.com")
    page.click("text=Register")
    

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
    assert post_response.data.decode('utf-8') == ""

def test_delete_spaces(db_connection, web_client):
    db_connection.seed("seeds/test_bamboo_bnb_directory.sql")
    delete_response = web_client.delete('/spaces', data={
        'id': 1
    })
    assert delete_response.status_code == 200
    repository = SpaceRepository(db_connection)
    assert repository.all() == [
        Space(2, 'space2', 'street2', 'city2', 'type2', 2, 2, 2, 200.00, 2),
        Space(3, 'space3', 'street3', 'city3', 'type3', 3, 3, 3, 300.00, 3),
    ]
