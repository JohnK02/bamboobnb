from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     p_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(p_tag).to_have_text("This is the homepage.")

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
    post_response = web_client.post('/spaces')
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == ""

    # get_response = web_client.get('/users')
    # assert get_response.status_code == 200
    # assert get_response.data.decode('utf-8') == "" \
    #     "Users(1, user1, password1, email1@email.com)\n" \
    #     "Users(2, user2, password1, email2@email.com)"

#      === End Example Code ===

# """
# /POST albums
# When I add a new album through POST /albums
# The album now shows with GET /albums
# """
# def test_post_albums(db_connection, web_client):
#     db_connection.seed('seeds/record_store.sql')
#     post_response = web_client.post('/albums', data={
#         'title': 'x',
#         'release_year': '2014',
#         'artist_id': '1'
#         })
#     assert post_response.status_code == 200
#     assert post_response.data.decode('utf-8') == ""

#     get_response = web_client.get('/albums')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#         "Album(1, +, 2011, 1)\n" \
#         "Album(2, x, 2014, 1)"
    
# def test_post_albums_with_error(db_connection, web_client):
#     db_connection.seed('seeds/record_store.sql')
#     post_response = web_client.post('/albums')
#     assert post_response.status_code == 400
#     assert post_response.data.decode('utf-8') == "" \
#         "You need to submit a title, release year and artist_id"

# """
# When I call GET /albums
# I get a list of albums back
# """
# def test_get_albums(db_connection, web_client):
#     db_connection.seed('seeds/record_store.sql')
#     response = web_client.get("/albums")
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == "" \
#         "Album(1, +, 2011, 1)"