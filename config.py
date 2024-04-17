from dotenv import load_dotenv
import os
load_dotenv()

class ApplicationConfig:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=r"sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    