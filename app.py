from flask_jwt_extended import create_access_token, create_refresh_token, decode_token, jwt_required, get_jwt_identity, JWTManager
from flask import Flask,jsonify,make_response,request,session
from flask_restful import Api,Resource
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from config import ApplicationConfig
from models import db,User

# Create a Flask application factory where I can intansitate  many flask applications
def create_app():
    app=Flask(__name__)
    app.config.from_object(ApplicationConfig)
    return app

app=create_app()

# Enable Cross-Origin Resource Sharing (CORS)
# **IMPORTANT**
# This should be extented during **DEPLOYMENT** 
# Failure all call CORS with the frontend application will be blocked
CORS(app)

# Initialize Flask-Migrate for database migrations
Migrate(app,db)

# Initialize Flask-Bcrypt for password hashing
bcrypt=Bcrypt(app)

# Initialize Flask-JWT-Extended for JWT authentication
jwt=JWTManager(app)

# Initialize the database connection
db.init_app(app)

# Initialize Flask-RESTful for creating API resources
api=Api(app)

# Create a welcome message resource
class Index(Resource):
    def get(self):
        return {"message":"Welcome to my API"}
    
api.add_resource(Index,'/')

# Create a user registration resource
class Register(Resource):
    def get(self):
        """
        Retrieve a list of all registered users.
        If no users are found, return an error message.
        """
        users=[user.to_dict() for user in User.query.all()]
        if not users:
            return make_response(jsonify({"error":"No users"}),400)
        return make_response(jsonify(users),200)

    def post(self):
        """
        Register a new user with the provided name, email, and password.
        Hash the password before storing it in the database.
        If a user with the same email already exists, return an error message.
        """
        data=request.get_json()
        password=data['password']
        email=data['email']
        name=data['name']
        hashed_password=bcrypt.generate_password_hash(password).decode('utf8')
        data['password']=hashed_password

        user_exists=User.query.filter_by(email=email).first()
        if user_exists:
            response = make_response(jsonify({"error": f"user with email {email} already exists"}), 401)
            return response

        new_user=User(**data)
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({"message":f"user {name} has been registered successfully"}),201)

api.add_resource(Register, '/register')

# Create a user login resource
class Login(Resource):
    def post(self):
        """
        Log in a user with the provided email and password.
        If the user does not exist, return an error message.
        If the password is incorrect, return an error message.
        If the login is successful, generate access and refresh tokens,
        store the user ID in the session, and return the tokens.
        """
        data=request.get_json()
        email=data['email']
        password=data['password']
        user=User.query.filter_by(email=email).first()
        if not user:
            return make_response(jsonify({"error":f"User {email} does not exist"}),401)
        if bcrypt.check_password_hash(user.password,password):
            session['user_id']=user.id
            access_token=create_access_token(identity=email)
            refresh_token=create_refresh_token(identity=email)
            response={
                "message":"Successfully logged in",
                "user":user.id,
                "access_token":access_token,
                "refresh_token":refresh_token,
            }
            return make_response(jsonify(response),201)
        else:
            return make_response(jsonify({"message":"Invalide password"}),404)

api.add_resource(Login,'/login')

# Run the Flask application
if __name__=='__main__':
    app.run(port=5000,debug=True)