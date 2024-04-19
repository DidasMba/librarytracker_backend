## Library Tracker Flask API 
Welcome to the Library Tracker Flask API ! This project provides a foundation for building RESTful APIs using Flask, Flask-RESTful, and other common Flask extensions. Whether you're new to Flask or looking for a structured starting point, this repository can help kickstart your API development journey.

## Purpose
The purpose of this project is to provide a codebase for  efficient and scalable RESTful APIs with Flask. The endpoints for user registration, login, are setup.

## Features
1. User registration and login endpoints
2. Token-based authentication using JWT
3. Secure password hashing with Flask-Bcrypt
4. Integration with SQLAlchemy for database management
5. Clear and structured codebase for easy understanding and customization

## Getting Started
To set up the Flask API on your local machine, follow these steps:

1. Fork the repository:
2. Clone the repository to local machine:
```bash
git clone git@github.com:<userName>/librarytracker_backend.git
```
3. Navigate to the directory:
```bash
cd librarytracker_backend
```
4. Enter vEnvironment
```bash
pipenv shell
```
5. Start the application
```bash
python3 app.py
```
Access the API at http://localhost:5000.
- API port can be changed in the app folder.

Set up the migrations file **only when making adjustments to the models files**

```bash
flask db init
flask db migrate
flask db upgrade.
```


For detailed documentation on API endpoints and usage, refer to the [API Documentation](./APIDOC/README.md).