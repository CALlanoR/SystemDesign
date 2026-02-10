# Dockerfile Structure

## Basic Structure
```dockerfile
# 1. Base Image (Operating System + Runtime)
# Defines the base image. This is the foundation and must always be the first line.
FROM python:3.12-slim

# 2. Working Directory (Where the code lives inside the container)
WORKDIR /app

# 3. Copy dependency files first (Cache Optimization)
COPY requirements.txt .

# 4. Execute commands (Installing libraries)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the source code
COPY . .

# 6. Environment Variables (Configuration)
ENV PYTHONUNBUFFERED=1

# 7. Port documentation
EXPOSE 8000

# 8. Defines the default executable for a running container. There can only be one CMD.
CMD ["python", "main.py"]
```

## The Concept of Layers and Caching
This is the most critical concept for optimizing deployment pipelines:
- **Layering**: Every instruction (FROM, RUN, COPY) creates a new layer.
- **Immutability**: Once a layer is built, it is cached. If you change a line in the Dockerfile, Docker rebuilds that specific layer and every subsequent layer.
- **Pro Tip**: This is why we copy requirements.txt and install dependencies before copying the rest of the source code. If you only change a line of logic in main.py, Docker will reuse the cached layers for your libraries, making the build significantly faster.
