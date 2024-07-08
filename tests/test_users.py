from lib.users import Users


def test_users_constructs():
    user= Users(1, "Test Username", "Test Password, Test Email")
    assert user.id == 1
    assert user.username == "Test Username"
    assert user.password == "Test Password"
    assert user.email == "Test Email"

def test_users_format_nicely():
    users = Users(1, "Test Username", "Test Password", "Test Email")
    assert str(users) == "(1, Test Username, Test Password, Test Email)"

def test_users_are_equal():
    user1 = Users(1, "Test Username", "Test Password", "Test Email")
    user2 = Users(1, "Test Username", "Test Password", "Test Email")
    assert user1 == user2


def test_users_validity():
    assert Users(1, "", "", "").is_valid() == False
    assert Users(1, "Username", "", "Email").is_valid() == False
    assert Users(1, "", "Password", "Email").is_valid() == False
    assert Users(1, "Username", None, "Email").is_valid() == False
    assert Users(1, None, "Password", "Email").is_valid() == False
    assert Users(1, "Username", "Password", "Email").is_valid() == True
    assert Users(None, "Username", "Password", "Email").is_valid() == True
    assert Users(1, "Username", "Password", "").is_valid() == False


def test_users_errors():
    assert Users(1, "", "", "").generate_errors() == "Username can't be blank, Password can't be blank, Email can't be blank"
    assert Users(1, "Username", "", "Email").generate_errors() == "Password name can't be blank"
    assert Users(1, "", "Password", "Email").generate_errors() == "Username can't be blank"
    assert Users(1, "Username", None, "Email").generate_errors() == "Password name can't be blank"
    assert Users(1, None, "Password", "Email").generate_errors() == "Username can't be blank"
    assert Users(1, "Username", "Password", "Email").generate_errors() == None
    assert Users(None, "Username", "Password", "Email").generate_errors() == None
    assert Users(1, "Username", "Password", "").generate_errors() == "Email can't be blank"
    assert Users(1, "Username", "Password", None).generate_errors() == "Email can't be blank"