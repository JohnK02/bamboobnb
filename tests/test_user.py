from lib.user import User


def test_users_constructs():
    user= User(1, "Test Username", "Test Password", "Test Email")
    assert user.id == 1
    assert user.username == "Test Username"
    assert user.password == "Test Password"
    assert user.email == "Test Email"

def test_users_format_nicely():
    users = User(1, "Test Username", "Test Password", "Test Email")
    assert str(users) == "User(1, Test Username, Test Password, Test Email)"

def test_users_are_equal():
    user1 = User(1, "Test Username", "Test Password", "Test Email")
    user2 = User(1, "Test Username", "Test Password", "Test Email")
    assert user1 == user2


def test_users_validity():
    assert User(1, "", "", "").is_valid() == False
    assert User(1, "Username", "", "Email").is_valid() == False
    assert User(1, "", "Password", "Email").is_valid() == False
    assert User(1, "Username", None, "Email").is_valid() == False
    assert User(1, None, "Password", "Email").is_valid() == False
    assert User(1, "Username", "Password", "Email").is_valid() == True
    assert User(None, "Username", "Password", "Email").is_valid() == True
    assert User(1, "Username", "Password", "").is_valid() == False


def test_users_errors():
    assert User(1, "", "", "").generate_errors() == "Username can't be blank, Password can't be blank, Email can't be blank"
    assert User(1, "Username", "", "Email").generate_errors() == "Password can't be blank"
    assert User(1, "", "Password", "Email").generate_errors() == "Username can't be blank"
    assert User(1, "Username", None, "Email").generate_errors() == "Password can't be blank"
    assert User(1, None, "Password", "Email").generate_errors() == "Username can't be blank"
    assert User(1, "Username", "Password", "Email").generate_errors() == None
    assert User(None, "Username", "Password", "Email").generate_errors() == None
    assert User(1, "Username", "Password", "").generate_errors() == "Email can't be blank"
    assert User(1, "Username", "Password", None).generate_errors() == "Email can't be blank"