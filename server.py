from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db, User, Rating
import crud
from jinja2 import StrictUndefined
import requests
import json,os

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")

@app.route("/sign_in")
def sign_in():
    """User login page"""

    return render_template("sign-in.html")


@app.route("/all_rests", methods=["POST"])
def process_login():
    """Process user login and show 10 restaurants"""

    email = request.form.get("email")
    password = request.form.get("password")

    print(email)
    print(password)

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("Unable to login with this email address and password. Check your login information and try again.")
        return redirect("/sign_in")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.fname} {user.lname}!")
        return render_template("all-rests.html")


@app.route("/sign_up")
def sign_up():
    """User sign up page"""

    return render_template("sign-up.html")


@app.route("/sign_up", methods=["POST"])
def process_sign_up():
    """Create a new user"""

    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    phone = request.form.get("phone")


    user1 = crud.get_user_by_email(email)
    user2 = crud.get_user_by_phone(phone)

    if user1:
        flash("An account is already associated with this email. Sign in to get started.")
    elif user2:
        flash("Mobile number already exists. Please try again with another one")
    elif phone and len(phone) != 10:
        flash("Phone number is of invalid format")
    elif password and len(password) < 8:
        flash("Password must contain at least 8 characters.")
    else:
        new_user = crud.create_user(email, password, phone, fname, lname)
        db.session.add(new_user)
        db.session.commit()
        flash("Your account was created successfully and you can now log in.")

    return redirect("/sign_up")


@app.route("/get_restaurants")
def get_rests_info():
    """Get restaurant info from Yelp API(default location Charlotte, NC 28226)"""

    #define the endpoint, API key and the header
    url = "https://api.yelp.com/v3/businesses/search"
    yelp_key = os.environ.get("YELP_KEY")
    HEADERS = {"Authorization": "bearer %s" % yelp_key}

    location = request.args.get("location")
    print (location)
    
    if not location:
        location = "28226"

    #define the parameters
    parameters = {
        "term" : "restaurants",
        "radius": "5000",
        "limit": "10",
        "location": location
    }

    restaurants = requests.get(url, params=parameters, headers=HEADERS).json()

    return(restaurants)





# @app.route("/users", methods = ["post"])
# def register_user():
#     """Create a new user"""

#    



# @app.route("/")
# def show_all_movies():
#     """View all movies"""

#     movies = crud.get_movies()

#     return render_template("all_movies.html", movies = movies)


# @app.route("/movies/<movie_id>")
# def show_movie(movie_id):
#     """Show details on a particular movie."""

#     movie = crud.get_movie_by_id(movie_id)

#     return render_template("movie_details.html", movie=movie)


# @app.route("/users")
# def show_all_users():
#     """View all users"""

#     users = crud.get_users()

#     return render_template("all_users.html", users=users)


# @app.route("/users/<user_id>")
# def show_user(user_id):
#     """Show user details"""
    
#     user = crud.get_user_by_id(user_id)

#     return render_template("user_details.html", user = user)




# @app.route("/movies/<movie_id>/ratings", methods=["POST"])
# def create_rating(movie_id):
#     """Create a new rating for the movie."""

#     logged_in_email = session.get("user_email")
#     print(logged_in_email)
#     rating_score = request.form.get("rating")

#     if logged_in_email is None:
#         flash("You must log in to rate a movie.")
#     elif not rating_score:
#         flash("Error: you didn't select a score for your rating.")
#     else:
#         user = crud.get_user_by_email(logged_in_email)
#         movie = crud.get_movie_by_id(movie_id)

#         rating = crud.create_rating(user, movie, int(rating_score))
#         db.session.add(rating)
#         db.session.commit()

#         flash(f"You rated this movie {rating_score} out of 5.")

#     return redirect(f"/movies/{movie_id}")




if __name__ == "__main__":
    # connect to database before app.run gets called. 
    # If not, Flask won’t be able to access your database
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
