from lib.users_repository import UsersRepository
from lib.users import Users

"""
When we call user repository,
we should get a list of user objects
reflecting this seed data
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/test_bamboo_bnb_directory.sql")
    repository = UsersRepository(db_connection)
    users = repository.all()
    assert users == [
        Users(1, 'user1', 'password1', 'email1@email.com'),
        Users(2, 'user2', 'password2', 'email2@email.com'),
        Users(3, 'user3', 'password3', 'email3@email.com')
    ]



"""
When we call UsersRepository #find
We get a single Users object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/test_bamboo_bnb_directory.sql")
    repository = UsersRepository(db_connection)

    users = repository.find(1)
    assert users == Users(1, 'user1', 'password1', 'email1@email.com')


def test_create_record(db_connection):
    db_connection.seed("seeds/test_bamboo_bnb_directory.sql")
    repository = UsersRepository(db_connection)

    repository.create(Users(4, 'user4', 'password4', 'email4@email.com'))

    result = repository.all()
    assert result == [
        Users(1, 'user1', 'password1', 'email1@email.com'),
        Users(2, 'user2', 'password2', 'email2@email.com'),
        Users(3, 'user3', 'password3', 'email3@email.com'),
        Users(4, 'user4', 'password4', 'email4@email.com')
    ]

def test_delete_record(db_connection):
    db_connection.seed("seeds/test_bamboo_bnb_directory.sql")
    repository = UsersRepository(db_connection)
    repository.delete(4)

    result = repository.all()
    assert result == [
        Users(1, 'user1', 'password1', 'email1@email.com'),
        Users(2, 'user2', 'password2', 'email2@email.com'),
        Users(3, 'user3', 'password3', 'email3@email.com')
    ]