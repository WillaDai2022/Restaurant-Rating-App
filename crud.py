"""CRUD operations."""

from model import db, User, Restaurant, Rating, connect_to_db


def create_user(email, password, phone, fname, lname):
    """Create and return a new user."""

    user = User(email=email, password=password, phone=phone, fname=fname, lname=lname)

    return user


def get_users():
    """Show all the users"""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user with a specific id"""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_restaurant(yelp_id, name, address, phone, review_count, price_range,
                    category, dietary, picture):
    """Create and return a new movie."""

    restaurant = Restaurant(
        yelp_id=yelp_id, 
        name=name, 
        address=address, 
        phone=phone, 
        review_count=review_count, 
        price_range=price_range,
        category=category, 
        dietary=dietary, 
        picture=picture,
    )

    return restaurant


def get_reataurants():
    """Return all movies."""

    return Restaurant.query.all()


def get_restaurant_by_id(restaurant_id):
    """Take a movie_id as an argument and return the movie with that ID."""

    return Restaurant.query.get(restaurant_id)


def create_rating(user, restaurant, pic, score, review):
    """create a rating to a movie by a user"""

    rating = Rating(user=user, restaurant=restaurant, pic=pic, 
                    score=score, review= review)
        
    return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)