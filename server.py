from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db, User, Word, Score
# import crud
# import seed_database as seed
from seed_database import create_user
from jinja2 import StrictUndefined
from flask import Flask, request, render_template, jsonify
import random
import datetime


# creating instance of a flask app
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def home_page():
    if 'name' in session:
        return redirect('/login')
    return render_template('homepage.html')



@app.route("/users", methods=["POST"])
def register_user():

    # POST == request.form => python dicts containing key/value pairs
    # GET == request.args => python dicts containing key/value pairs
    email = request.form.get("email") # request.form['email']
    password = request.form.get("password")

    # For login =>> 
    # SELECT email FROM users WHERE email="test123@gmail.com";
    existing_user = User.query.filter(User.email==email).first()
     # querying users table for the user with that email

    # check if user with that email already exists in the database
        # if user doesn't exist, then create a user
    # user = seed.create_user(email, password)
    # user = create_user(email, password) # returns an instance of a User object

    if existing_user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = create_user(email, password)
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
        return redirect("/login")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")
        return redirect("/game")


@app.route("/game")
def game_page():
    # query the database for all words
    words = Word.query.all()
    # maybe query for five letter words
    random_word = random.choice(words)
    ### something like => Word.query.all() => gives us a list of all word records from database
    # use random.choice() to grab a random word
    # pass that random word to the template (keyboard.html)

    # when a new random word is grabbed from db, save to session
    session["word_id"] = random_word.word_id

    return render_template("keyboard.html", random_word=random_word)


@app.route("/profile")
def user_profile():

    # querying the database for the user's scores
    # returning to the template "games played" "games won"
    email = session["user_email"]
    current_user = User.query.filter(User.email==email).first()
    # current_user.scores

    return render_template("profile.html", current_user=current_user)


@app.route("/scores", methods=['POST'])
def user_score():
    # from the fetch, need to pass data: how many guesses? did they get it right?

    # this route will handle updating score when the user gets it right/runs out of guesses
    word_id = session['word_id']
    word_date = datetime.datetime.now().date()
    num_guesses = request.json.get("num-guesses") #integer
    is_win = request.json.get("is_win") #true or false
    user_email = session['user_email']

    current_user = User.query.filter(User.email==user_email).first()

    # create a new Score() => word 
    score = Score(user_id=current_user.user_id, word_id=word_id, word_date=word_date, num_guesses=num_guesses, is_win=is_win)
    # return render_template("profile.html", user_score=user_score)
    db.session.add(score)
    db.session.commit()

    return {
        "success": True
    }

# @app.route("/words.json")
# def word_page():
#     words = Word.query.all()
#     words_list = WORDS
   



    # return redirect ("/")

    # processing login (ratings lab has good examples)
    # checking if user exists => User.query.filter(...) # querying users table for the user with that email and password
    # add user to flask session => reference login session from ratings lab

    # return render_template()
    



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
