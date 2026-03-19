PROJECT REPORT

Title:
Stayease – A Hotel Booking Backend System
(Task 01: Basic REST API with CRUD Operations)


Objective:
To initiate the development of Stayease, a hotel booking backend system, by implementing a foundational REST API that performs CRUD operations on user data using FastAPI, following a clean and scalable architecture.


Tech Stack:
- Python
- FastAPI
- Uvicorn
- Pydantic


Features Implemented (Task 01):
- Create a new user
- Retrieve all users
- Retrieve a single user by ID
- Update user details
- Delete a user
- Input validation (email format)
- Duplicate email prevention
- Proper HTTP status codes and error handling


Project Structure:
backend/
│
├── app/
│   ├── main.py
│   ├── schemas/
│   │   └── user_schema.py
│   ├── routes/
│   │   └── user_routes.py
│   ├── services/
│       └── user_service.py
│
├── requirements.txt


API Endpoints:

| Method | Endpoint           | Description        |
|--------|--------------------|--------------------|
| POST   | /users             | Create a new user  |
| GET    | /users             | Get all users      |
| GET    | /users/{user_id}   | Get user by ID     |
| PUT    | /users/{user_id}   | Update user        |
| DELETE | /users/{user_id}   | Delete user        |


Sample Request:

Create User:
{
  "name": "Peauli",
  "email": "test@gmail.com",
  "age": 21
}


Error Handling:

400 Bad Request:
- Invalid email format
- Duplicate email

404 Not Found:
- User does not exist


Key Concepts Learned:
- REST API design principles
- CRUD operations in backend systems
- FastAPI routing and modular architecture
- Data validation using Pydantic
- Separation of concerns (schemas, services, routes)
- Handling real-world constraints such as duplicate data


Limitations (Current Stage):
- Data is stored in memory (non-persistent)
- No authentication or role-based access
- No database integration
- Only user module implemented


Future Scope:
- Integrate database (SQLite/PostgreSQL)
- Implement JWT authentication
- Add user roles (customer and manager)
- Develop hotel, room, and booking modules
- Implement search and filtering
- Add caching for performance optimization


Conclusion:
Task 01 establishes the foundation of the Stayease backend system by implementing a structured and scalable REST API. This phase focuses on core backend principles that will support future enhancements such as database integration, authentication, and full booking functionality.