import os
from flask import Flask, request, render_template, url_for, redirect
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.users_repository import UsersRepository
from lib.spaces_repository import SpaceRepository
from lib.space import Space

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/', methods=['GET'])
def get_home():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.all()
    return render_template('home.html', spaces=spaces)

@app.route('/registration', methods = ['GET'])
def post_register():
    return render_template('users/registration.html')

@app.route('/login', methods = ['GET'])
def get_login():
    return render_template('users/login.html')

@app.route('/users', methods=['POST'])
def post_users():
    if has_invalid_users_parameters(request.form):
        return  "You need to submit a username, password and email", 400
    connection = get_flask_database_connection(app)
    repository = UsersRepository(connection)

    users = User(
        None,
        request.form['username'],
        request.form['password'],
        request.form['email'],
        )
    repository.create(users)
    return redirect("/login")


def has_invalid_users_parameters(form):
    return 'username' not in form or \
    'password' not in form \
    or 'email' not in form 

@app.route('/spaces', methods=['GET'])
def get_spaces():
    return render_template('spaces/create_space.html')

@app.route('/spaces/<id>', methods=['GET'])
def get_spaces_id(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    space = repo.find(id)
    return render_template('spaces/show.html', space=space)

@app.route('/spaces', methods=['POST'])
def post_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    repository.create(Space(
        None,
        request.form['name'],
        request.form['street'],
        request.form['city'],
        request.form['property_type'],
        request.form['maximum_capacity'],
        request.form['number_of_bedrooms'],
        request.form['number_of_bathrooms'],
        request.form['price_per_night'],
        request.form['user_id'],
        ))
    # return "\n".join(
    #     f"{space}" for space in repository.all())
    return '', 200

@app.route('/spaces', methods=['DELETE'])
def delete_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    repository.delete(request.form['id'])
    return "\n".join(
        f"{space}" for space in repository.all())

@app.route('/about', methods=['GET'])
def get_about():
    return render_template('users/about.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
