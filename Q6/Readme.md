# Lab Question 6: Multi-Container Application with Docker Compose

## 📝 Problem Statement
**Design and deploy a multi-container application using Docker Compose by creating an application service and a dependent database/Redis service, configuring service dependencies, networks, and volumes, and verifying inter-container communication.**

---

## ✅ Solution Steps

Follow these steps to set up and run the multi-container application.

### Step 1: Project Files Setup
We have created the following files in this directory:

1.  **`app.py`**: A Flask application that connects to a Redis service to track page views.
2.  **`requirements.txt`**: Lists `flask` and `redis` dependencies.
3.  **`Dockerfile`**: Instructions to build the Python application image.
4.  **`docker-compose.yml`**: The orchestration file that defines two services:
    *   `web`: The Flask app (built from the local Dockerfile).
    *   `redis`: The database (pulled from the official Redis image).

### Step 2: Explain `docker-compose.yml`
Open [docker-compose.yml](docker-compose.yml) to understand the configuration:

*   **Services**: `web` and `redis`.
*   **Depends On**: Note that `web` depends on `redis`, ensuring Redis starts first.
*   **Networks**: Both services share `app-network` to communicate (the web app connects to host `redis`).
*   **Volumes**: The `web` service maps the current directory (`.`) to `/app` inside the container for live updates.

### Step 3: Start the Application
Open your terminal in this directory (`Q6`) and use Docker Compose to build and start the services.

```bash
docker-compose up --build -d
```
*   `--build`: Forces a re-build of the images.
*   `-d`: Runs containers in detached mode (background).

### Step 4: Verify the Deployment

1.  **Check Running Containers:**
    ```bash
    docker-compose ps
    ```
    You should see two containers (`Q6_web` and `Q6_redis`) in the "Up" state.

2.  **Test the Application:**
    Open your browser to: [http://localhost:5000](http://localhost:5000)
    
    *   Refresh the page multiple times.
    *   You should see the "Hello from Docker Compose!" message and the view counter increasing (1, 2, 3...), confirming the `web` container is successfully talking to the `redis` container.

3.  **Check Logs:**
    To see the logs from specific services:
    ```bash
    docker-compose logs -f web
    ```

### Step 5: Stop and Clean Up
To stop the services and remove the containers and networks:

```bash
docker-compose down
```
