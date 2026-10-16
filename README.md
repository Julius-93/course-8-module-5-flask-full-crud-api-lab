# Module Lab: Building Full CRUD RESTful APIs with Flask

## Learning Goals

- Implement RESTful API endpoints using Flask.
- Handle HTTP POST, PATCH, and DELETE methods to manage resource data.
- Accept and process JSON input using `request.get_json()`.
- Simulate persistent data using in-memory Python objects.
- Follow RESTful route conventions and return structured JSON responses.

## Introduction

In this lab, you will build a **Full CRUD API** to manage a list of events. The API will allow users to:

- Create new events using `POST`
- Update existing events using `PATCH`
- Delete events using `DELETE`

You’ll simulate database-like behavior with in-memory Python class objects and respond to all client requests with properly formatted JSON and appropriate status codes.

This lab reinforces essential backend development skills including route design, data mutation, error handling, and RESTful conventions.

## Setup Instructions

### Fork and Clone the Repository

1. Go to the provided GitHub repository link.
2. Fork the repository to your GitHub account.
3. Clone the forked repository to your local machine:

```bash
git clone <repo-url>
cd course-8-module-5-flask-full-crud-api-lab
```

### Install Dependencies

Ensure Python is installed:

```bash
python --version
```

Install Flask and dependencies using pipenv:

```bash
pipenv install
pipenv shell
```

Or with pip:

```bash
pip install flask
```

## Tasks

### Task 1: Define the Problem

You’re building a basic event management API. It should:

- Accept event creation via `POST /events`
- Allow updating event titles via `PATCH /events/<id>`
- Delete events using `DELETE /events/<id>`
- Respond with structured JSON and appropriate HTTP status codes

---

### Task 2: Determine the Design

The Flask API should be structured as follows:

- Use `@app.route()` with correct HTTP method decorators
- Accept input using `request.get_json()`
- Represent data using a custom `Event` class
- Store events in an in-memory list
- Use `jsonify()` for consistent JSON responses

---

### Task 3: Develop the Code

Create `app.py` and start with the following structure:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Event class
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory data store
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: POST /events - Create a new event from JSON input
# TODO: PATCH /events/<id> - Update the title of an event
# TODO: DELETE /events/<id> - Remove an event from the list

if __name__ == "__main__":
    app.run(debug=True)
```

---

### Task 4: Test the API

Start the Flask development server:

```bash
python app.py
```

Test your endpoints using Postman or curl:

- `POST http://localhost:5000/events`
  - Body: `{ "title": "Hackathon" }`
- `PATCH http://localhost:5000/events/1`
  - Body: `{ "title": "Hackathon 2025" }`
- `DELETE http://localhost:5000/events/2`

---

## Best Practices

- Use RESTful nouns in routes (e.g., `/events`)
- Validate incoming JSON and handle missing keys gracefully
- Use helper functions to reduce code repetition
- Return:
  - `201 Created` for successful POST
  - `200 OK` or `204 No Content` for PATCH and DELETE
  - `404 Not Found` if a resource doesn't exist
- Include inline comments to explain logic

---

## Considerations

**1. Input Validation**
- Ensure the `title` field is provided.
- Return a `400 Bad Request` if missing.

**2. Event Not Found**
- Return `404 Not Found` with a clear message when the event ID doesn't exist.

**3. Reusable Logic**
- Consider writing a helper function to look up events by ID.

**4. Scalability**
- While using a single file works here, separate concerns into modules as your API grows.

---

## Conclusion

After completing this lab, you will:

✅ Know how to handle incoming JSON with Flask  
✅ Build routes that implement full CRUD behavior  
✅ Simulate persistent resource changes in memory  
✅ Return proper HTTP status codes and structured responses  

This is a critical step in your backend developer journey. Next up: persistent databases!


# Flask Full CRUD RESTful API

## Project Overview

This project is a RESTful API developed using Python and Flask. It provides functionality for creating, retrieving, updating, and deleting events.

The application demonstrates fundamental backend development concepts, including HTTP methods, request processing, JSON serialization, input validation, error handling, and CRUD operations.

The project was developed as part of the Moringa School Full Stack Software Engineering programme.

## Technologies Used

* Python 3.11
* Flask
* Pipenv
* Pytest
* Git and GitHub
* RESTful APIs
* JSON

## Project Objectives

The objectives of this project are to:

1. Implement RESTful API endpoints using Flask.
2. Process incoming JSON requests.
3. Simulate database operations using Python objects.
4. Implement POST, GET, PATCH, and DELETE methods.
5. Validate incoming data.
6. Handle missing resources appropriately.
7. Write testable and maintainable backend code.

## API Endpoints

| HTTP Method | Endpoint       | Description               |
| ----------- | -------------- | ------------------------- |
| GET         | `/events`      | Retrieve all events       |
| GET         | `/events/<id>` | Retrieve a specific event |
| POST        | `/events`      | Create a new event        |
| PATCH       | `/events/<id>` | Update an existing event  |
| DELETE      | `/events/<id>` | Delete an existing event  |

The GET endpoints are optional extensions to the original lab requirements.

## Installation

Clone your fork of the repository and navigate into the project directory.

Install the project dependencies:

`pipenv install`

## Running the Application

Start the Flask development server:

`pipenv run python app.py`

The application will be accessible at:

`http://127.0.0.1:5000`

## Example API Request

### Creating an Event

**Endpoint:** POST `/events`

Request body:

```json
{
  "title": "Python Workshop"
}
```

Successful response:

```json
{
  "id": 3,
  "title": "Python Workshop"
}
```

HTTP Status: `201 Created`

### Updating an Event

**Endpoint:** PATCH `/events/1`

Request body:

```json
{
  "title": "Advanced Python Workshop"
}
```

HTTP Status: `200 OK`

### Deleting an Event

**Endpoint:** DELETE `/events/2`

HTTP Status: `204 No Content`

## Error Handling

The API handles invalid requests using standard HTTP status codes.

| Status Code | Meaning                        |
| ----------- | ------------------------------ |
| 200         | Request processed successfully |
| 201         | Resource created successfully  |
| 204         | Resource deleted successfully  |
| 400         | Invalid request data           |
| 404         | Requested resource not found   |

## Testing

The application uses Pytest for automated testing.

Run the test suite using:

`pipenv run python -m pytest -v`

The original lab includes five automated tests covering event creation, updating, deletion, and handling nonexistent events.

## Project Structure

```text
course-8-module-5-flask-full-crud-api-lab/
├── tests/
│   └── test_app.py
├── app.py
├── Pipfile
├── Pipfile.lock
├── pytest.ini
└── README.md
```

## Design Considerations

**Input Validation:** The API checks that event titles are valid, non-empty strings before creating or updating events.

**Error Handling:** Requests involving nonexistent resources return HTTP 404 responses.

**Code Reusability:** Helper functions are used to locate events and validate incoming data, reducing unnecessary duplication.

**Data Storage:** Events are stored in an in-memory Python list. This simulates basic database operations without requiring a database server.

**Maintainability:** The application uses clearly separated functions, consistent naming conventions, and explanatory comments.

## Limitations and Future Improvements

The current application uses in-memory storage, meaning data is lost when the application restarts.

Potential improvements include integrating PostgreSQL or SQLite, adding authentication, implementing pagination, expanding automated tests, and organizing the application using Flask Blueprints.

## Conclusion

This project demonstrates the implementation of a RESTful API using Flask. It provides practical experience with HTTP methods, JSON processing, CRUD operations, data validation, error handling, and automated testing.
