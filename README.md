# Django TDD demo

The application provides a basic example of how to structure a Django project with a focus on TDD and Docker.

## Features

*   Basic Django setup
*   Example models, views, and serializers
*   Comprehensive unit tests
*   Docker configuration
*   Configured to use PostgreSQL
 
## Setup Instructions

1.  **Clone the repository:**

    ```
    git clone https://github.com/ali-abbaszade/tdd-django.git
    ```

2.  **Build and run the Docker containers:**

    ```
    docker-compose up --build
    ```

    This command will build the Docker image and start the containers for the Django application and the PostgreSQL database.

3.  **Apply migrations:**

    ```
    docker-compose exec app python manage.py migrate
    ```

    This command applies the database migrations to set up the database schema.
