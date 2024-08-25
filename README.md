## Task 6.2

```bash
docker build --tag books-catalog:1 .
kubectl config current-context
# Should be docker-desktop
kubectl apply -f scripts/deployment.yml

kubectl get pods
kubectl get deployments
kubectl get services

kubectl logs books-catalog-546c89679b-k76tj

kubectl delete -f scripts/deployment.yml
```
