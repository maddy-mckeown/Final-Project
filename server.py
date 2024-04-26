from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db, User
# import crud
# import seed_database as seed
from seed_database import create_user
from jinja2 import StrictUndefined

# creating instance of a flask app
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def home_page():
    if 'name' in session:
        return redirect('/login')
    return render_template('homepage.html')

# Model ~ View ~ Controller
@app.route('/some-url', methods=['GET', 'POST']) # method that creates a route/URL/path; methods means what type of request
def get_some_page_name(): # view function, view meaning it renders something to the browser
    # return something a browser can understand
    # browsers can understand text, html, json
    # return render_template('some-html.html')
    # return redirect('/some-other-url') # redirecting to another url (@app.route) that renders a template
    return ''

@app.route("/users", methods=["POST"])
def register_user():

    # POST == request.form => python dicts containing key/value pairs
    # GET == request.args => python dicts containing key/value pairs
    email = request.form.get("email") # request.form['email']
    password = request.form.get("password")

    # user = seed.create_user(email, password)
    user = create_user(email, password) # returns an instance of a User object
    # For login =>> User.query.filter(email==email) # querying users table for the user with that email and password
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        # user = seed.create_user(email, password)
        # adding user to database
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/login")


@app.route("/login", methods=['GET'])
def login_page():
    return render_template("login.html")

@app.route("/user_login", methods=['POST'])
def user_login_page():
    email = request.form.get("email") # request.form['email']
    password = request.form.get("password")

    user = User.query.filter(User.email == email).first()
 
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/game")

@app.route("/game")
def game_page():
       return render_template("game.html")

    # return redirect ("/")

    # processing login (ratings lab has good examples)
    # checking if user exists => User.query.filter(...) # querying users table for the user with that email and password
    # add user to flask session => reference login session from ratings lab

    # return render_template()
    




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
