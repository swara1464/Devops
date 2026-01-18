# Lab Question 4: Deploying to Kubernetes

## 📝 Problem Statement
**Deploy the previously created Docker image on Kubernetes using a Deployment YAML file. Verify that the pod is running using `kubectl` commands. Expose the application using a NodePort Service, access it using the node’s IP and port, and scale the deployment to 3 replicas using `kubectl scale`.**

---

## ✅ Solution Steps

Follow these steps to deploy and manage your application on Kubernetes.

### Prerequisites
*   Ensure you have a Kubernetes cluster running (e.g., Minikube, Docker Desktop).
*   Ensure the Docker image `student-portal:v1` is available to your cluster.
    *   *If using Minikube:* Run `minikube image load student-portal:v1`
    *   *If using Docker Desktop:* It should be available automatically if built locally.

### Step 1: Create the Deployment
Use the `deployment.yaml` file to create the pod.

```bash
# Apply the deployment configuration
kubectl apply -f deployment.yaml
```

**File:** [deployment.yaml](deployment.yaml)

### Step 2: Verify the Pod is Running
Check the status of your deployment and pods.

```bash
# Get Deployments
kubectl get deployments

# Get Pods (Wait for status to be 'Running')
kubectl get pods
```

### Step 3: Expose the Application
Use the `service.yaml` file to create a NodePort service.

```bash
# Apply the service configuration
kubectl apply -f service.yaml
```

**File:** [service.yaml](service.yaml)

**Verify Service:**
```bash
kubectl get services
```

### Step 4: Access the Application
Access the application using `NodeIP:NodePort`.

*   **Cluster IP / localhost:** `http://localhost:30007` (if using Docker Desktop)
*   **Minikube:**
    ```bash
    # Get the URL directly
    minikube service flask-app-service --url
    ```

### Step 5: Scale the Deployment
Scale the number of pods from 1 to 3.

```bash
# Scale to 3 replicas
kubectl scale deployment flask-app-deployment --replicas=3

# Verify the new pods
kubectl get pods
```

You should now see 3 pods running for your application.
