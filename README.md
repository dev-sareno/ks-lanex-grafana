# ks-lanex-grafana
Introducing Grafana & Prometheus to Lanex DevOps team. The goal is to rollout this technology to all projects after the KS.

## Directory structure
### [argocd/](./argocd)
Kubernetes YAML files for deploying applications. ArgoCD reads from this directory.

### [jsapp/](./jsapp)
Contains the code for Express.js (JavaScript) based example Prometheus metrics.

### [pyapp/](./pyapp)
Contains the code for Flask (Python) based example Prometheus metrics.
