
## Detailed Endpoint Documentation:
### Welcome Message Endpoint (/):
- GET:
- Description: Retrieves a welcome message.
- Response:
    - Status Code: 200 OK
    - Response Body:
    ```bash
    { "message": "Welcome to my API" }
    ```
     
### User Registration Endpoint (/register):
- POST:
- Description: Registers a new user with provided details.
- Request Body:
     ```bash
     name (string): User's name.
    ```
     ```bash
     email (string): User's email address.
    ```
     ```bash
     password (string): User's password.
    ```
      
- Response:
    - Status Code:
        - 201 Created: User successfully registered.
        - 401 Unauthorized: User with the same email already exists.
    - Response Body:
        ```bash
        { "message": "User [name] has been registered successfully" } (if successful),
        ```
        ```bash
        { "error": "User with email [email] already exists" } (if user already exists)
        ```
        
- GET:
- Description: Retrieves a list of all registered users.
- Response:
    - Status Code:
        - 200 OK: Users retrieved successfully.
        - 400 Bad Request: No users found.
    - Response Body:
        ```bash
        List of user objects, each containing user details (id, name, email).
        ```
### User Login Endpoint (/login):
- POST:
- Description: Logs in a user with provided credentials.
- Request Body:
    - email (string): User's email address.
    - password (string): User's password.
- Response:
    - Status Code:
        - 201 Created: Login successful.
        - 401 Unauthorized: User does not exist or incorrect password.
    - Response Body:
        ```bash
        { "message": "Successfully logged in", "user": [user_id], "access_token": [JWT_access_token], "refresh_token": [JWT_refresh_token] } (if successful)
        ```
         ```bash
        { "error": "User [email] does not exist" } (if user does not exist)
        { "message": "Invalid password" } (if incorrect password)
        ```
        
### Additional Information:
- Authentication:
User registration and login endpoints require valid credentials.
Authentication is handled using JSON Web Tokens (JWT).
- Error Handling:
Detailed error messages are provided for different scenarios (e.g., user already exists, invalid password).
- Validation:
User input validation is performed for email addresses and passwords to ensure data integrity.