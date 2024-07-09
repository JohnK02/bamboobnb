from lib.users import Users

class UsersRepository:

    def __init__(self, connection):
        self._connection = connection

    # Retrieve all users
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = Users(row["id"], row["username"],row["password"], row["email"])
            users.append(item)
        return users

    # Find a single user by its id
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [id])
        row = rows[0]
        return Users(row["id"], row["username"],row["password"], row["email"])

    # Create a new users
    def create(self, user):
        rows = self._connection.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s) RETURNING id', [
                                    user.username, user.password, user.email])
        row = rows[0]
        user.id = row["id"]
        return user

    # Delete a users by its id
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [id])
        return None