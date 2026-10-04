# Python REST API

A simple REST API built with Python and FastAPI.

This project demonstrates how to build a REST API, validate incoming data using Pydantic, containerize the application using Docker, and manage the project using Git and GitHub.

## Technologies

- Python
- FastAPI
- Uvicorn
- Pydantic
- Docker
- Git
- GitHub

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Returns a welcome message |
| GET | `/users` | Returns the list of users |
| POST | `/users` | Creates a new user after validating the request data |


### Request Example

For `POST /users`:

```json
{
  "name": "Lydia",
  "email": "lydia@example.com"
}



### Validation

The API uses Pydantic to validate incoming user data.

Both name and email are required fields.

Docker

The application is containerized using Docker.

A Dockerfile is used to:

Use Python 3.12 as the base image
Install the required dependencies
Copy the application code into the image
Expose port 8000
Start the FastAPI application using Uvicorn
Build the Docker Image
docker build -t python-rest-api .
Run the Container
docker run --name python-rest-api -p 8000:8000 python-rest-api

The API can then be accessed at:

http://localhost:8000/docs