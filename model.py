"""Models for restaurant ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tabalename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)

    ratings = db.relationship("Rating", back_populates="user")
    fav_rests = db.relationship("Fav_rest", back_populates="user")

    def __repr__(self):
        "Show user_id and user_name"

        return f"<user_id: {self.user_id} user_name: {self.fname} {self.lname}>"

class Fav_rest(db.Model):
    """User's favorite restaurant -- associate table"""

    __tablename__ = "fav_rest"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.restaurant_id"), nullable=False)

    user = db.relationship("User", back_populates="fav_rests")
    restaurant = db.relationship("Restaurant", back_populates="fav_rests")
    
class Restaurant(db.Model):
    """A restaurent"""

    __tablename__ = "restaurant"

    restaurant_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    yelp_id = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)

    ratings = db.relationship("Rating", back_populates="restaurant")
    fav_rests = db.relationship("Fav_rest", back_populates="restaurant")

class Rating(db.Model):
    """A restaurant rating"""

    __tablename__ = "rating"

    rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.column(db.String(100))
    pic = db.Column(db.Text)
    score = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.restaurant_id"), nullable=False)

    user = db.relationship("User", back_populates="ratings")
    restaurant = db.relationship("Restaurant", back_populates="ratings")


def connect_to_db(flask_app, db_uri="postgresql:///restaurant_guide", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)




