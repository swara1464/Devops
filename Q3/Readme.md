# Lab Question 3: Dockerizing a Web Application

## 📝 Problem Statement
**Create a simple web application (HTML or Python Flask). Write a Dockerfile, build a Docker image, and run the container so the application is accessible on a browser using port mapping. Using Docker commands, perform the following operations:**
*   List images and containers
*   Stop a running container
*   Remove a container and image
*   Demonstrate commands like: `docker ps`, `docker stop`, `docker rm`, `docker rmi`

---

## ✅ Solution Steps

Follow these steps to complete the task.

### Step 1: Create Application Files
We have created a simple Python Flask application for this task.
*   `app.py`: The web application code.
*   `requirements.txt`: Dependencies (Flask).
*   `Dockerfile`: Instructions to build the image.

### Step 2: Build the Docker Image
Open your terminal in this directory (`Q3`) and run the build command.

```bash
# syntax: docker build -t <image_name> .
docker build -t my-flask-app .
```
*   `-t my-flask-app`: Tags the image with the name "my-flask-app".
*   `.`: Specifies the current directory as the build context.

### Step 3: Run the Container
Run the container based on the image you just built, mapping port 5000 of the container to port 5000 on your host machine.

```bash
# syntax: docker run -d -p <host_port>:<container_port> --name <container_name> <image_name>
docker run -d -p 5000:5000 --name flask-container my-flask-app
```
*   `-d`: Runs the container in detached mode (background).
*   `-p 5000:5000`: Maps host port 5000 to container port 5000.
*   `--name flask-container`: Assigns a specific name to the container.

**Verify:** Open your browser and visit `http://localhost:5000`. You should see "Hello from Docker!".

### Step 4: Manage Docker Containers and Images
Now, perform the requested operations using Docker commands.

#### 1. List Containers and Images
Check the running containers and the list of available images.

```bash
# List running containers
docker ps

# List all containers (including stopped ones)
docker ps -a

# List all local Docker images
docker images
```

#### 2. Stop the Container
Stop the running Flask container.

```bash
# syntax: docker stop <container_name_or_id>
docker stop flask-container
```

#### 3. Remove the Container
Once stopped, remove the container to free up resources.

```bash
# syntax: docker rm <container_name_or_id>
docker rm flask-container
```

#### 4. Remove the Image
If you no longer need the application image, you can remove it.

```bash
# syntax: docker rmi <image_name_or_id>
docker rmi my-flask-app
```
