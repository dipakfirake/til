# AWS EC2 vs ECS vs EKS vs Lambda

> _2026-06-26_ | Category: **cloud**

Choosing AWS compute.

| Service | Level | What you manage | Best For |
|:---|:---|:---|:---|
| **EC2** | IaaS | OS, updates, scaling, network | Legacy apps, deep control |
| **ECS** | CaaS | Docker containers | Microservices, Docker |
| **EKS** | CaaS | Kubernetes clusters | Large, complex k8s workloads |
| **Lambda**| FaaS | Just code | Event-driven, cron, APIs |

**Key Takeaway**: Start Serverless (Lambda/Fargate ECS). Only move to EC2/EKS when you need specific OS control, persistent background processes, or have massive predictable scale where serverless gets too expensive.
