# SIT722 - Task 6.2

## GitHub Link

[https://github.com/adriangabardo/agabardo-sit722-part2](https://github.com/adriangabardo/agabardo-sit722-part2)

## Instructions

**Set $DATABASE_URL environment variable:**

- Go to scripts/deployment.yml
- Replace `$DATABASE_URL` with your PostgreSQL DB URL

```bash
# Build Docker image
docker build --tag books-catalog:1 .

# Ensure Kubernetes context is docker-desktop
kubectl config current-context

# Deploy Kubernetes resources from template file
kubectl apply -f scripts/deployment.yml

# Ensure everything is running accordingly
kubectl get pods
kubectl get deployments
kubectl get services

# Otherwise check logs for container
kubectl logs $POD_CONTAINER_ID

# Delete all Kubernetes resources
kubectl delete -f scripts/deployment.yml
```
