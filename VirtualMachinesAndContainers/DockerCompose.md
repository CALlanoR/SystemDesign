# Docker Compose
While a Dockerfile is used to build a single image, Docker Compose is the orchestrator used to define and run multi-container applications. In your current workflow.

1. The Core Structure
A docker-compose.yml file uses YAML syntax and is generally divided into four top-level sections:
    - **services**: Defines the containers (e.g., your Python app, MongoDB, Redis).
    - **networks**: Defines how containers talk to each other.
    - **volumes**: Defines persistent data storage.
    - **configs/secrets**: Handles sensitive data or configuration files.
    - **Dependencies**: You can define dependencies between services using the depends_on keyword, ensuring that services start in the correct order.

2. Common Commands
    - **docker-compose up**: Starts all the services defined in your docker-compose.yml file.
    - **docker-compose up -d**: Runs containers in the background (detached mode).
    - **docker-compose down**: Stops and removes all the services.
    - **docker-compose build**: Builds the images for all the services.
    - **docker-compose ps**: Lists all the services and their status.
    - **docker-compose logs**: Displays the logs for all the services.

4. Example

```yaml
version: '3.8'

services:
  # Service 1: Your Database
  database:
    image: mongo:latest
    container_name: mongodb_service
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: user_architect
      MONGO_INITDB_ROOT_PASSWORD: secure_password
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

  # Service 2: Your Python Application
  app:
    build: .  # Points to the Dockerfile in the current directory
    container_name: python_app_service
    depends_on:
      - database  # Ensures the DB starts before the app
    environment:
      - MONGO_URI=mongodb://user_architect:secure_password@database:27017/
    volumes:
      - .:/app  # Hot-reloading: maps local code to container for development
```


