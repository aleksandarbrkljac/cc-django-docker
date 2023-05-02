# Django + Docker Faculty Project - Web Application for Managing Student Enrollment

This is a faculty project that demonstrates the integration of Django web framework with Docker for easy deployment and development. The web application is designed to manage student enrollment in courses, exams, and consultations for multiple faculties.

## Project Specification

For detailed information about the project requirements and objectives, please refer to the [Project Specification](specifikacija.pdf) document.

## Features

- Django web application framework
- Docker containerization for simplified development and deployment
- Customizable settings for different environments
- User authentication and role-based access control
- Management of courses, exams, and consultations
- Student enrollment in courses and exams
- Viewing and exporting course and exam schedules
- Support for multiple faculties with separate databases and web applications

## Prerequisites

Ensure you have the following installed on your system:

- Docker: https://docs.docker.com/get-docker/
- Docker Compose: https://docs.docker.com/compose/install/

## Services and Containers

The project uses the following services and containers:

- `pgadmin`: pgAdmin web interface for managing PostgreSQL databases
- `ftndb`, `pmfdb`, `pravnidb`, `unsdb`: PostgreSQL databases for each faculty and the university
- `ftnssluzba`, `pmfssluzba`, `pravnissluzba`: Django web applications for each faculty
- `unssluzba`: Node.js-based university API

## Getting Started

1. Clone the repository:

```
    git clone https://github.com/Aleksandar9999/cc-django-docker.git
```

2. Change to the project directory:

```
    cd cc-django-docker
```

3. Build and run the Docker containers:

```
    docker-compose up --build
```

4. Access the Django web applications for each faculty at:

- FTN: `http://localhost:8081`
- PMF: `http://localhost:8082`
- PRAVNI: `http://localhost:8083`

5. Access the Node.js-based UNS application at `http://localhost:3000`.

6. Access the pgAdmin interface at `http://localhost:5050`. Use the email `admin@admin.com` and password `root` to log in.

## Customizing Environment Settings

You can customize the environment settings by modifying the `.env` file. The file contains environment variables that can be used to change the behavior of the application.

## Stopping the Application

To stop the running containers, press `CTRL+C` in the terminal window where `docker-compose up` was executed.

To remove the containers and associated volumes, run:

```
    docker-compose down -v
```
