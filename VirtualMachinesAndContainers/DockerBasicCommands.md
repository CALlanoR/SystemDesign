# Docker

## Install Docker
    - https://docs.docker.com/get-docker/

## Install Docker-Compose
    - https://docs.docker.com/compose/install/

## Official docker release:
    - https://www.youtube.com/watch?v=zgR8otZkwHc
    - https://www.youtube.com/watch?v=wW9CAH9nSLs

## Docker Hub
    - https://hub.docker.com/

# Basic Docker Commands

## List running containers
    - sudo docker ps
    - sudo docker ps -a

## Create a simple nginx container
    - sudo docker run -dit --name my-running-app -p 9090:80 nginx:latest
        - where -d: detached, -i: interactive, -t: pseudo-TTY, -p: port mapping

## Get logs from a container
    - sudo docker logs my-running-app

## Get stats from a container
    - sudo docker stats my-running-app

## Get top processes running inside a container
    - sudo docker top my-running-app

## Get port mapping of a container
    - sudo docker port my-running-app

## Get information about a container
    - sudo docker inspect my-running-app

## Exec into a container
    - sudo docker exec -it my-running-app bash

## Stop a container
    - sudo docker stop my-running-app

## Start a container
    - sudo docker start my-running-app

## Remove a container
    - sudo docker rm my-running-app

## Remove a running container
    - sudo docker rm -f my-running-app

## Remove all stopped containers
    - sudo docker container prune

## Images 1
    - sudo docker images
    - sudo docker rmi <<IMAGE_ID>>
    - sudo docker image prune  # Delete dangling images
    - sudo docker image prune -a  # Delete all unused images
    - sudo docker image prune -a -f # Force delete all unused image

## Dockerfile basic website example
```html
<!DOCTYPE html>
<html>
<head>
    <title>Clase Cloud Computing</title>
    <style>
        body { font-family: sans-serif; text-align: center; background-color: #f4f4f4; }
        h1 { color: #2c3e50; }
    </style>
</head>
<body>
    <h1>Hi from my docker container Nginx!</h1>
    <p>Docker basic commands</p>
</body>
</html>
```

```dockerfile
FROM nginx:alpine

LABEL maintainer="wachu@javerianacali.edu.edu"

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
```

- sudo docker build -t my_website_image . 
- sudo docker images
- sudo docker run -d -p 8080:80 --name my-running-app2 my_website_image


## Understanding Image Types (Alpine, Slim, Distroless, Scratch)
- Choosing the right base image is about balancing security, size, and compatibility.
    - **Full (Standard)**: Based on full OSs like Ubuntu. They include package managers (apt), shells (bash), and tools like curl or git. Best for development.
    - **Slim**: A stripped-down version of the Full image. It removes manuals and non-essential packages but keeps the package manager.
    - **Alpine**: Tiny (~5MB) and highly secure. It uses musl libc instead of glibc. Perfect for microservices.
    - **Distroless**: Created by Google. They only contain your application and its runtime. No shell, no package manager. Extremely secure.
    - **Scratch**: An explicitly empty image (0 bytes). Used for statically compiled binaries (like those in Go or Rust).


## Images 2
- sudo docker tag my_website_image:latest my_website_image:v1.0
- sudo docker save my_website_image:v1.0 -o my_website_image.tar
- sudo docker load -i my_website_image.tar