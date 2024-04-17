from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
import re

db=SQLAlchemy()

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
email_pattern=r'^[a-zA-Z]+\.[a-zA-Z]+@strathmore\.edu$'
phone_pattern=r'^\+\d{12}$'

class User(db.Model,SerializerMixin):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(64),nullable=False)

    @validates
    def validate_email(self,key,email):
        if not re.match(email_pattern,email):
            raise ValueError("Invalid email address")
        return email

    @validates
    def validate_password(self,key,password):
        if len(password)<8:
            raise ValueError("short password")
        return password