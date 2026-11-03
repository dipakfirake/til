# Kubernetes Basics - Pods and Deployments

> _2026-11-03_ | Category: **devops**

Container orchestration fundamentals.

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels: { app: my-app }
  template:
    metadata:
      labels: { app: my-app }
    spec:
      containers:
        - name: app
          image: myapp:1.0.0
          ports: [{ containerPort: 8080 }]
          resources:
            requests: { cpu: "100m", memory: "128Mi" }
            limits: { cpu: "500m", memory: "512Mi" }
          livenessProbe:
            httpGet: { path: /health, port: 8080 }
            initialDelaySeconds: 30
---
apiVersion: v1
kind: Service
metadata:
  name: my-app-svc
spec:
  selector: { app: my-app }
  ports: [{ port: 80, targetPort: 8080 }]
  type: ClusterIP
```

```bash
kubectl apply -f deployment.yaml
kubectl get pods
kubectl logs my-app-xxx
kubectl scale deployment my-app --replicas=5
```
