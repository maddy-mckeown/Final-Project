import os
import json
from random import choice, randint
from datetime import datetime
from model import db, User, connect_to_db
from flask import Flask, request, render_template, jsonify




import model

import requests

# res = requests.get('https://random-word-api.vercel.app/')

# search_results = res.json()
# app.app_context().push()
# model.connect_to_db(app)
# model.db.create_all()







def get_word_list(word_length):
    url = "https://random-word-api.vercel.app/api"
    params = {
        "words": 500,
        "length": word_length
    }
    # https://random-word-api.vercel.app/api?words=500&length=5
    response = requests.get(url, params=params)
    if response.status_code == 200:
        word_list = response.json()
        for word in word_list: # word_list = ["bingo", "trunk", "lapse"......]
            new_word = model.Word(word_id=word, letter_count=word_length, word_score=word_length) # word_id, letter_count, word_score
             # Assuming Word has a 'word' attribute
            # check if word already in database
            if model.Word.query.get(word) is None: #checks if word in database already
                model.db.session.add(new_word)
                model.db.session.commit()
        return word_list
    else:
        return []


# word_list_5 = get_word_list(5)
# word_list_6 = get_word_list(6)
# word_list_7 = get_word_list(7)
# print(get_word_list)


# for n in range(10):
#     email = f'user{n}@test.com' 
#     password = 'test'



def create_user(email, password, user_tokens=0):
    """Creates an instance of a User
    
    Note: Creates User object from model.py
    """
    # email and password come from server where we call the create_user() function
    user = model.User(email=email, password=password, user_tokens=user_tokens)

    return user


def get_users():


    return User.query.all()

    # create a user => email, password (user_tokens, user_level)
    # user = model.User() # todo fill this in

    # You don't need a crud file
    # user = crud.create_user(email, password)
    # model.db.session.add(user)

    # for _ in range(10):
    #     word_id = choice(Word)
    #     score = int(1, 5)  #level?


    model.db.session.commit()


if __name__ == '__main__':
    from server import app


    app.app_context().push()
    model.connect_to_db(app)

    word_list_5 = get_word_list(5)
    # word_list_6 = get_word_list(6)
    # word_list_7 = get_word_list(7)
    print(get_word_list)

    for n in range(10):
        email = f'user{n}@test.com' 
        password = 'test'
        user = create_user(email, password)
        db.session.add(user)
    db.session.commit()

