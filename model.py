"""Models for restaurant ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tabalename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    passowrd = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)

    ratings = db.relationship("Rating", back_populates="user")

    def __repr__(self):
        "Show user_id and user_name"

        return f"<user_id: {self.user_id} user_name: {self.user_name}>"


class Restaurant(db.Model):
    """A restaurent"""

    __tablename__ = "restaurant"

    restaurant_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    yelp_id = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    review_count = db.Column(db.Integer, nullable=False)
    price_range = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String,nullable=False)
    dietary = db.Column(db.String)
    picture = db.Column(db.Text,nullable=False)

    ratings = db.relationship("Rating", back_populates="restaurant")


class Rating(db.Model):
    """A restaurant rating"""

    __tablename__ = "rating"

    rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pic = db.Column(db.Text)
    score = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.restaurant_id"), 
                            nullable=False)

    user = db.relationship("User", back_populates="ratings")
    restaurant = db.relationship("Restaurant", back_populates="ratings")


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
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




