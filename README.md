# TODO-List Server

A simple TODO-List Server with REST API endpoints for managing TODO items. Users can sign in using Gmail login. Built with Python Django Framework and SQLite.

## Features

- User authentication with Gmail.
- Add a TODO item.
- Delete a TODO item.
- List all TODO items.
- Mark a TODO item as completed.

## Requirements

- Python 3.11
- SQLite
- Docker & Docker-Compose

## Getting Started

### Running the App

1. Clone the repository:

    ```bash
    git clone https://github.com/samcarmen/to-do.git
    ```

2. Navigate to the project directory:

    ```bash
    cd todo_backend
    ```

3. Start the Docker containers:

    ```bash
    docker-compose up
    ```

Your app should now be running at `http://localhost:8000`.

### Testing the App

#### Authentation:

To test Google authentication, please follow these steps:

1. Send an email to carmen.samkahman@gmail.com with your intended email address to be used for testing. This will allow you to be added to the list of authorized test users.
2. Once added, open your web browser and navigate to http://localhost:8000/login.
3. Log in using the registered email address.
4. After a successful login, you will be directed to the home page, where your DRF token will be displayed.

#### TO-DO API Endpoints:

List all TODOs: 

Retrieve a list of all TODO items.
```bash
curl -H "Authorization: Token [your drf token]" http://localhost:8000/todo/todos/

```

Add a TODO: 

Add a new TODO item to the list.
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Token [your DRF token]" -d '{"description": "test"}' http://localhost:8000/todo/add/

```

Delete a TODO: 

Delete a specific TODO item by its ID.
```bash
curl -X DELETE -H "Authorization: Token [your DRF token]" http://localhost:8000/todo/{id}/delete/

```

Mark TODO as Complete: 

Mark a specific TODO item as complete by its ID.
```bash
curl -X PATCH -H "Authorization: Token [your DRF token]" http://localhost:8000/todo/{id}/complete/

```

Note: After making changes using the "Add," "Delete," or "Mark as Complete" endpoints, refresh the home page to see the updates reflected.

## Unit Tests
Unit tests have been implemented to thoroughly test the functionality of both Google logins and each of the API endpoints. This ensures the robustness of the application's features.

To run the unit tests, use the following commands:

For testing Google logins:
```bash
python manage.py test todo.tests.auth_tests   
```

For testing API endpoints:
```bash
python manage.py test todo.tests.todo_tests   
```