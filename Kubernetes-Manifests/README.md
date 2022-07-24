```
kubectl apply -f operator/
```

```
kubectl apply -f letsencrypt-prod.yaml
```

```
echo $(kubectl get secret queue-db-default-user -n microservices -o jsonpath='{.data.username}' | base64 --decode)
echo $(kubectl get secret queue-db-default-user -n microservices -o jsonpath='{.data.password}' | base64 --decode)
echo $(kubectl get secret --namespace "kong" kong-postgresql -o jsonpath="{.data.password}" | base64 --decode)
```

```
kubectl create namespace kong
helm install kong kong/ -n kong -f kong-lb-db-adm-values.yaml
export NIP_IP=$(kubectl get -o jsonpath="{.status.loadBalancer.ingress[0].ip}" service -n kong kong-kong-proxy | tr "." -)
```

```
helm install konga konga/ -n kong
```

```
kubectl create namespace microservices
helm install microservices microservices/ -n microservices --set nipIPAddress=$NIP_IP
```
