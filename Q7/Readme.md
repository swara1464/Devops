# Expose & Scale Application (NodePort)

This guide details how to expose your running Kubernetes deployment to the outside world (or local network) using a **NodePort Service** and how to scale the application to handle more load.

## Prerequisites

Before proceeding, ensure that:
1.  **Kubernetes Cluster** is running (`kubectl cluster-info`).
2.  **Deployment** from the previous step (Q6) is active.
    *   Verify with: `kubectl get deployments student-portal-deploy`
    *   If not, go back to Q6 and apply the deployment first.

---

## Configuration

The service configuration is defined in `service-nodeport.yaml`.

*   **File:** [`service-nodeport.yaml`](./service-nodeport.yaml)
*   **Type:** `NodePort`
*   **Target Port:** `5000` (Container port)
*   **Node Port:** `30080` (External access port)

---

## Step 1: Expose the Application

Apply the service configuration to create the NodePort service.

### 1. Navigate to the Directory
```bash
cd d:/CLi/Devops/Q7
```

### 2. Apply the Service
```bash
kubectl apply -f service-nodeport.yaml
```

**Expected Output:**
```text
service/student-portal-nodeport created
```

---

## Step 2: Access the Application

Once the service is created, you can access the application using the Node's IP address and the defined port (`30080`).

### 1. Find the URL

*   **If using Minikube:**
    Run the following command to get the exact URL instantly:
    ```bash
    minikube service student-portal-nodeport --url
    ```

*   **If using Docker Desktop / Standard K8s:**
    Use `localhost` (if port forwarding is auto-managed) or the Node IP.
    ```bash
    http://localhost:30080
    ```
    OR
    ```bash
    # Get Node IP
    kubectl get nodes -o wide
    # Access via <NODE-IP>:30080
    ```

### 2. Test Accessibility
You can test the connection using `curl` or your browser:

```bash
curl http://<YOUR-NODE-IP>:30080
```

**Expected Output:**
You should see the HTML response from your application (e.g., `<!doctype html>...`).

---

## Step 3: Scale the Deployment

To handle more traffic, scale the application to 3 replicas.

### 1. Run Scale Command
```bash
kubectl scale deployment student-portal-deploy --replicas=3
```

**Expected Output:**
```text
deployment.apps/student-portal-deploy scaled
```


### 2. Verify Scaling
Check that 3 pods are now running:

```bash
kubectl get pods -l app=student-portal
```

**Expected Output:**
```text
NAME                                     READY   STATUS    RESTARTS   AGE
student-portal-deploy-66b8c6f5f9-abcde   1/1     Running   0          5m
student-portal-deploy-66b8c6f5f9-bghij   1/1     Running   0          10s
student-portal-deploy-66b8c6f5f9-klmno   1/1     Running   0          10s
```

### 3. Verify Service Endpoints
Ensure the service is correctly routing to your pods (endpoints should match your pods' IPs):

```bash
kubectl get endpoints student-portal-nodeport
```

---

## Troubleshooting

*   **Service External IP is `<pending>`:** This is normal for NodePort/LoadBalancer types in some environments (like Minikube or bare metal). You should access it via the Node IP (or `minikube ip`).
*   **Connection Refused:**
    *   Ensure the pods are `Running` (`kubectl get pods`).
    *   Check if `minikube tunnel` is needed (for LoadBalancer, though usually not for NodePort, but sometimes required on Mac/Windows).
    *   Verify the firewall allows traffic on port `30080`.
*   **Pods stuck in `Pending`:** You might not have enough resources (CPU/Memory) in your cluster. Try scaling down to 2 replicas.

---

## Cleanup (Uninstallation)

To remove the service and scale back down:

```bash
# Delete the service
kubectl delete -f service-nodeport.yaml

# Scale back to 1 replica (optional)
kubectl scale deployment student-portal-deploy --replicas=1
```
