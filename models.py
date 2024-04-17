from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

db=SQLAlchemy()

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})


class User(db.Model,SerializerMixin):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(64),nullable=False)