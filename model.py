"""
Note from Ray:
- complete the User, Word, and UserWord table per our first draft of data model
- think through Scores OR Games OR GamesPlayed tables => which do we need?
--- goal is to expand on basic concept of what's missing from wordle
"""

# I don't think we need a games played table - the word_id will tell us if they've played that game already


# import the sqlalchemy library

# instantiate db object
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users" # whatever tablename we include here becomes the tablename in postgres

    # tablename_id => unique identifier for records in this table
    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    # user_level = db.Column(db.Integer)
    user_tokens = db.Column(db.Integer)

    scores = db.relationship('Score', back_populates='user')

    # User.query.get(1).scores => return all score records for a given user
    # In the seed_database.py file, you can seed users the same way as the ratings lab

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Word(db.Model):
     
    __tablename__ = "words"

    word_id = db.Column(db.String(25),
                        primary_key=True)
    letter_count = db.Column(db.Integer)
    word_score = db.Column(db.Integer)

    scores = db.relationship('Score', back_populates="word")
    # possible_guesses
    def __repr__(self):
        return f'<Word word_id={self.word_id} letter_count={self.letter_count}>'


    # In the seed_database.py file, you will make a request to the random word generator api
    # Link to requests library from lecture: https://fellowship.hackbrightacademy.com/materials/serft24/lectures/apis/#introducing-requests

    # Then with the response, you create a word_list
    # for word in word_list => word_list == what you got from the api
    #   new_word = Word(word_name="brittle", letter_count=7)
    #   db.session.add(new_word)
    #   db.session.commit()


    # __tablename__ => plural lowercase table na

class Score(db.Model): ## turn this into Scores? - seems like a down the road thing

    __tablename__ = "scores"

    score_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True, )
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    word_id = db.Column(db.String, db.ForeignKey('words.word_id')) # foreign key
    word_date = db.Column(db.Date)
    num_guesses = db.Column(db.Integer)
    is_win = db.Column(db.Boolean)
    # can revisit word if they don't pass the level

    # # db.relationship('NameOfClass', ) => method that navigates the foreign key relationship, goes to the other table, queries the other table at the same time
    user = db.relationship('User', back_populates="scores")
    # # Score.users => all users
    word = db.relationship('Word', back_populates="scores")
    
    def __repr__(self):
        return f'<Score score_id={self.score_id} word_date={self.word_date}>'

    # # SEMI RELEVANT TO YOUR CODE
    # users = db.relationship('User', back_populates="scores")
    # # you have a user logged into your app that's user #3
    # Score.query.filter_by(user_id=3).all() # all scores associated with that user
    # # db.relationship => set up users
    # # you want to query for all users who have received the word "bingo"
    # Score.query.filter_by(word_id='bingo').users => return all user records, otherwise it would be a join
    #

    
# class Games_Played(db.Model):

#     __tablename__ = "Games Played"

#     user_id = db.Column(db.Integer,
#                         autoincrement=True,
#                         primary_key=True, )
#     game_id = db.Column(db.Integer, unique=True, )
#     gmplayed = db.Column(db.Integer)
#     date = db.Column(db.Date, back_populates="user")
#     wstreak = db.Column(db.Integer)
#     #do i need a lose streak?
#     game_score = db.Column(db.Integer)



# def __repr__(self):
#         return f'<User user_id={self.user_id} game_id={self.game_id} gmplayed={self.gmplayed}
            
    
def connect_to_db(flask_app, db_uri="postgresql:///Wordled", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    # per Flask docs, include the app's context (JUST a flask inconsistency)
    # this line helps flask know its own identity
    app.app_context().push()
    connect_to_db(app)
       

