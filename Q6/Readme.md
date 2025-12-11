# Student Portal Kubernetes Deployment

This repository contains the necessary Kubernetes configuration files to deploy the **Student Portal** application (or a placeholder `nginx` service) to a Kubernetes cluster.

## Prerequisites

Before running the code, ensure you have the following installed and set up on your machine:

1.  **Kubernetes Cluster**:
    *   You can use **Minikube**, **Docker Desktop (Kubernetes enabled)**, of a cloud provider (GKE, EKS, AKS).
    *   Ensure your cluster is running: `kubectl cluster-info`

2.  **kubectl CLI**:
    *   Install the Kubernetes command-line tool to interact with your cluster.
    *   [Installation Guide](https://kubernetes.io/docs/tasks/tools/)

3.  **Terminal**:
    *   Use bash, PowerShell, or any standard terminal interface.

---

## Configuration

The deployment settings are defined in `deployment.yaml`. 

*   **File:** [`deployment.yaml`](./deployment.yaml)
*   **Default Image:** `nginx:latest` (This is a placeholder. If you have a custom image like `student-portal:v1`, you should update this file).
*   **Port:** The container is configured to expose port `5000`.

To change the Docker image:
1.  Open `deployment.yaml`.
2.  Locate the line `image: nginx:latest`.
3.  Replace `nginx:latest` with your specific image name (e.g., `your-docker-username/student-portal:v1`).

---

## Installation Steps

Follow these steps to deploy the application:

### 1. Navigate to the Directory
Open your terminal and navigate to the folder containing these files:
```bash
cd d:/CLi/Devops/Q6
```
*(Adjust the path if you are on a different operating system or location)*

### 2. Apply the Deployment
Run the following command to create the deployment in your cluster:

```bash
kubectl apply -f deployment.yaml
```

**Expected Output:**
```text
deployment.apps/student-portal-deploy created
```

---

## Usage & Verification

Once deployed, verify that everything is running correctly.

### 1. Check Deployment Status
Ensure the deployment controller has accepted the configuration:

```bash
kubectl get deployments
```

**Expected Output:**
```text
NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
student-portal-deploy   1/1     1            1           10s
```

### 2. Check Pod Status
Verify that the pods are up and status is `Running`:

```bash
kubectl get pods -l app=student-portal
```

**Expected Output:**
```text
NAME                                     READY   STATUS    RESTARTS   AGE
student-portal-deploy-66b8c6f5f9-abcde   1/1     Running   0          25s
```

### 3. Check Logs (Optional)
If you need to troubleshoot, view the logs of your pod. First, get the pod name from the previous step, then run:

```bash
kubectl logs <pod-name>
```

---

## Cleanup (Uninstallation)

To remove the deployment and all associated resources from your cluster, run:

```bash
kubectl delete -f deployment.yaml
```
