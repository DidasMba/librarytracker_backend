from flask_jwt_extended import create_access_token, create_refresh_token, decode_token, jwt_required, get_jwt_identity, JWTManager
from flask import Flask,jsonify,make_response,request,session
from flask_restful import Api,Resource
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from config import ApplicationConfig
from models import db,User

def create_app():
    app=Flask(__name__)
    app.config.from_object(ApplicationConfig)
    return app

app=create_app()
CORS(app)
Migrate(app,db)
bcrypt=Bcrypt(app)
jwt=JWTManager(app)
db.init_app(app)
api=Api(app)


class Index(Resource):
    def get(self):
        return {"message":"Welcome to my API"}
    
api.add_resource(Index,'/')


# Endpoint to 
class Register(Resource):
    def get(self):
        users=[user.to_dict() for user in User.query.all()]
        if not users:
            return make_response(jsonify({"error":"No users"}),400)
        return make_response(jsonify(users),200)
    
    def post(self):
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

class Login(Resource):
    def post(self):
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


if __name__=='__main__':
    app.run(port=5000,debug=True)