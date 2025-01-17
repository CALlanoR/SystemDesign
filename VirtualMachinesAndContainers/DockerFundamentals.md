+ Install Docker
    - https://docs.docker.com/get-docker/

+ Install Docker-Compose
    - https://docs.docker.com/compose/install/

+ Official docker release:
    - https://www.youtube.com/watch?v=zgR8otZkwHc
    - https://www.youtube.com/watch?v=wW9CAH9nSLs

=========================================================================================

+ Docker Hub
    - https://hub.docker.com/

+ images
    - sudo docker images
    - sudo docker rmi <<IMAGE_ID>>
    - sudo docker image prune  # Delete dangling images
    - sudo docker image prune -a  # Delete all unused images
    - sudo docker build -t my_website_image . 
    - sudo docker tag <<IMAGE_NAME>> <<IMAGE_NAME>>:<<TAG>> 
        - Example: sudo docker tag my_website_httpd_image my_website_httpd_image:1.0
    - sudo docker save <<IMAGE_NAME>>:<<TAG>> > <<FILE_NAME.tar>>
    - sudo docker load -i <<FILE_NAME.tar>>

+ Containers
    - sudo docker ps -a
    - sudo docker start <<NAME or CONTAINER_ID>>
    - sudo docker stop <<NAME or CONTAINER_ID>>
    - sudo docker rm <<NAME or CONTAINER_ID>>
    - sudo docker rm -f <<NAME or CONTAINER_ID>>  # Delete a running container
    - sudo docker logs <<NAME or CONTAINER_ID>>
    - sudo docker exec -ti <<NAME or CONTAINER_ID>> bash
    - sudo docker run -di -p HOST_PORT:CONTAINER_PORT --name=<<NAME>> <<IMAGE_NAME>>  # Create container with image
    - sudo docker container prune  # Delete stopped containers
    - sudo docker stop $(sudo docker ps -aq)  # Stop all containers
    - sudo docker cp TARGET CONTAINER_ID:SOURCE  # docker cp index.html web:/index.html
    - sudo docker rename OLD_NAME NEW_NAME
    - sudo docker stats  # View stats of all containers
    - sudo docker top <<CONTAINER_ID>>
    - sudo docker port <<CONTAINER_ID>>

+ Volumes
    - docker volume ls
    - docker volume inspect
    - docker volume prune
    - docker volume rm

+ Build
    - sudo docker build -t <<IMAGE_NAME>> .

+ Inspect
    - sudo docker inspect <<CONTAINER_ID>>
    - sudo docker inspect --format '{{ .NetworkSettings.IPAddress }}' <<CONTAINER_ID>>

+ Examples:
    Note: To verify open ports: netstat -natp

    + sudo docker run -it ubuntu:latest /bin/bash

    + Python (https://hub.docker.com/_/python)
        - sudo docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3.9 python python_script.py

    + C/C++ (Operating System Environment)
        - sudo docker run -di --name mySOEnvironment ubuntu:latest /bin/bash
          Note: Two options:
            1. Install manually each package of docker.sh in vagrant_environment folder
            2. Create image with the same instructions
               2.1 Create Dockerfile
               2.2 sudo docker build -t operating_system .
               2.3 sudo docker run -di --name mySOEnvironment -v $(pwd)/examples:/examples operating_system:latest /bin/bash
               2.4 sudo docker exec -ti mySOEnvironment /bin/bash
               2.5 gcc -o fork00 process/fork00.c

    + MySQL (https://hub.docker.com/_/mysql)
        - sudo docker run -p 3306:3306 --name myMySQL5.7Test -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
        - sudo docker inspect myMySQL
        - use the ip in mysql workbech
        - sudo docker logs myMySQL

        - sudo docker run -p 3307:3306 --name MySQL8Test -e MYSQL_ROOT_PASSWORD=root -d mysql:8.0.27
        - sudo docker inspect MySQL8Test
        - In DBeaver:
             - activate SSL (Use SSL and Allow public key retrieval)
             - empty Database

    + PostgreSQL (https://hub.docker.com/_/postgres)
        - sudo docker run --name postgresql -e POSTGRES_PASSWORD=root -d postgres:14.0

    + Nginx (https://hub.docker.com/_/nginx)
        - View web -> docker -> static_website_with_http2

    + RabbitMQ (https://hub.docker.com/_/rabbitmq)
        - sudo docker run -d -p 15672:15672 --hostname my-rabbit --name myRabbit rabbitmq:3-management
        - sudo docker inspect myRabbit
        - http://container-ip:15672 in a browser 
        - guest/guest

    + httpd (https://hub.docker.com/_/httpd)
        - sudo docker run -dit --name my-running-app -p 9090:80 httpd:2.4

    + python-flask
        -View python_flask folder