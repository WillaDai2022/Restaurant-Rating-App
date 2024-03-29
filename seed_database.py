"""Script to seed database."""

import os
import json
import crud
import model
import server
from random import choice

os.system("dropdb restaurant_guide")
os.system("createdb restaurant_guide")

model.connect_to_db(server.app)
model.db.create_all()

# Load user data from JSON file
with open("data/users.json") as f:
    user_data = json.loads(f.read())

# Create users, store them in list so we can use them
users_in_db = []
for user in user_data:
    user_name, password, email, phone, fname, lname = (
        user["user_name"],
        user["password"],
        user["email"],
        user["phone"],
        user["fname"],
        user["lname"]
    )

    db_user = crud.create_user(email, user_name, password, phone, fname, lname)
    users_in_db.append(db_user)

# Add all users to database
model.db.session.add_all(users_in_db)
model.db.session.commit()


#create ratings for the user
with open("data/users.json") as f:
    ratings_data = json.loads(f.read())

for rating in ratings_data:
    title, pic, score, review = (
        rating["title"],
        rating["pic"],
        rating["score",
        rating["review"]]
    )

    rating = crud.create_rating(choice(users_in_db), title, pic, score, review)
    model.db.session.add(rating)

model.db.session.commit()