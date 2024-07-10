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

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/', methods=['GET'])
def get_home():
    return render_template('home.html')

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
    return '', 200

def has_invalid_users_parameters(form):
    return 'username' not in form or \
    'password' not in form \
    or 'email' not in form 

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
    return "\n".join(
        f"{space}" for space in repository.all())
    # return redirect(url_for('get_home')) 


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
