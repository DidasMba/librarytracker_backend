from flask import Flask,jsonify,make_response
from flask_restful import Api,Resource
from flask_cors import CORS
from flask_migrate import Migrate
from config import ApplicationConfig
from models import db

def create_app():
    app=Flask(__name__)
    app.config.from_object(ApplicationConfig)
    return app

app=create_app()
CORS(app)
Migrate(app,db)
api=Api(app)


class Index(Resource):
    def get(self):
        return {"message":"Welcome to my API"}
    
api.add_resource(Index,'/')


if __name__=='__main__':
    app.run(port=5000,debug=True)