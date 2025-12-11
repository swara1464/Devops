# Docker Operations Guide

This guide details the steps to manage Docker containers and images using the command line.

## 1. List Images and Containers

### List Running Containers
To view currently active containers:
```bash
docker ps
```
**Example Output:**
```
CONTAINER ID   IMAGE             COMMAND        CREATED         STATUS       PORTS                    NAMES 
d9f1c3a2b4e7   student-portal:v1 "python app.py"  2 minutes ago   Up 2 mins    0.0.0.0:5000->5000/tcp   student-portal 
```

### List All Containers
To view all containers, including stopped ones:
```bash
docker ps -a
```

### List Images
To view all available docker images:
```bash
docker images
```
**Example Output:**
```
REPOSITORY        TAG    IMAGE ID    CREATED    SIZE 
student-portal    v1     a1b2c3d4e5f6 2 hours ago 100MB 
```

## 2. Stop a Running Container
To stop a container that is currently running (replace `student-portal` with your container name or ID):
```bash
docker stop student-portal
```
**Output:**
```
student-portal 
```

## 3. Remove a Container and Image

### Remove a Container
First, ensure the container is stopped. Then remove it:
```bash
docker rm student-portal
```
**Output:**
```
student-portal 
```

### Remove an Image
To remove a specific docker image (replace `student-portal:v1` with your image name and tag):
```bash
docker rmi student-portal:v1
```
**Example Output:**
```
Untagged: student-portal:v1 
Deleted: sha256:a1b2c3... 
```

## 4. Setup if No Containers/Images Exist
If you find no containers or images are available, you can "download" (access) the **Q4 Student Portal** from this git ->https://github.com/Chinmayabs224/DevOps.git project and run it to have a working container environment.

### Steps to Setup Q4 Application

1. **Navigate to the Q4 Directory**
   Move from the current directory to the Q4 directory:
   ```bash
   cd ../Q4
   ```

2. **Build the Docker Image**
   Build the image from the Q4 source code:
   ```bash
   docker build -t student-portal:v1 .
   ```

3. **Run the Container**
   Start the container in detached mode with port mapping:
   ```bash
   docker run -d --name student-portal -p 5000:5000 student-portal:v1
   ```

Now you can proceed with the operations listed in sections 1-3.
