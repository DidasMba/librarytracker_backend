from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
import re

# Initialize the SQLAlchemy database instance
db = SQLAlchemy()

# Set up the naming convention for foreign keys
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Define the regular expression pattern for a valid email address
email_pattern = r'^[a-zA-Z]+\.[a-zA-Z]+@strathmore\.edu$'

# Define the regular expression pattern for a valid phone number
phone_pattern = r'^\+\d{12}$'

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    # The unique identifier for the user
    id = db.Column(db.Integer, primary_key=True)
    # The name of the user, which must be unique and cannot be null
    name = db.Column(db.String(50), unique=True, nullable=False)
    # The email address of the user, which must be unique and cannot be null
    email = db.Column(db.String(120), unique=True, nullable=False)
    # The password of the user, which cannot be null
    password = db.Column(db.String(64), nullable=False)

    # Validate the email address of the user
    @validates('email')
    def validate_email(self, key, email):
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email address")
        return email

    # Validate the password of the user
    @validates('password')
    def validate_password(self, key, password):
        if len(password) < 8:
            raise ValueError("Short password")
        return password