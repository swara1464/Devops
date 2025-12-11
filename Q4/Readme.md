# Dockerized Flask Application Guide

This guide details the steps to create, containerize, and run a fast, modern Flask web application using Docker.

## Project Overview

We will build a Student Portal registration application with a modern, responsive UI, containerize it using Docker, and run it with port mapping.

### Directory Structure

```text
student-portal/
├── app.py
├── requirements.txt
├── Dockerfile
└── templates/
    └── index.html
```

---

## Step 1: Create the Application

### 1. `app.py`
This is the main Flask application entry point. We have enhanced it to serve a proper HTML template.

File: [`app.py`](./app.py)

### 2. `templates/index.html`
Create a folder named `templates` and add `index.html`. This file contains the enhanced UI with modern styling.

File: [`templates/index.html`](./templates/index.html)

### 3. `requirements.txt`
Specify the dependencies.

File: [`requirements.txt`](./requirements.txt)

---

## Step 2: Containerize with Docker

### `Dockerfile`
Create a `Dockerfile` in the root directory to define the image.

File: [`Dockerfile`](./Dockerfile)

---

## Step 3: Build and Run

Open your terminal in the directory containing these files.

### 1. Build the Docker Image
This command reads the Dockerfile and builds an image named `student-portal` with tag `v1`.

```bash
docker build -t student-portal:v1 .
```

*Expected Output:*
```text
[+] Building 2.5s (10/10) FINISHED
...
 => writing image sha256:...
 => naming to docker.io/library/student-portal:v1
```

### 2. Run the Container
Run the container in detached mode (`-d`), mapping host port 5000 to container port 5000.

```bash
docker run -d --name student-portal -p 5000:5000 student-portal:v1
```

*Expected Output:*
```text
a1b2c3d4e5f6... (container ID)
```

### 3. Stop the Container
To stop the application, run:

```bash
docker stop student-portal
```

---

## Step 4: Verify

You can verify the application is running by accessing it in your browser or using `curl`.

### Browser
Open [http://localhost:5000](http://localhost:5000)

### Terminal (Curl)
```bash
curl -s http://localhost:5000 | head -n 15
```

*Expected Output (Snippet):*
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    ...
    <title>Student Portal</title>
```
