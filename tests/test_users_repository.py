from lib.users_repository import UserRepository
"""
When #all is called all of the user instances are returned
"""

def test_all(db_connection):
    db_connection.seed("seeds/test_bamboo_bnb_directory.sql")
    repo = UserRepository(db_connection)
    result = repo.all()
    assert result == [
        User('user1', 'password1', 'email1@email.com'),
        User('user2', 'password2', 'email2@email.com'),
        User('user3', 'password3', 'email3@email.com')
    ]