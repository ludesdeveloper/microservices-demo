# DEPLOYMENT

### **How To**

1. Install all operator
   > Cert Manager, Kubegress, RabbitMQ

```
kubectl apply -f operator/
```

2. Apply cluster issuer to get https certificate

```
kubectl apply -f letsencrypt-prod.yaml
```

3. Install kong and export nip.io ip address

```
kubectl create namespace kong
helm install kong kong/ -n kong -f kong-lb-db-adm-values.yaml
export NIP_IP=$(kubectl get -o jsonpath="{.status.loadBalancer.ingress[0].ip}" service -n kong kong-kong-proxy | tr "." -)
```

4. Install konga dashboard

```
helm install konga konga/ -n kong
```

5. Install all microservices

```
kubectl create namespace microservices
helm install microservices microservices/ -n microservices --set nipIPAddress=$NIP_IP
```

### **Additional Command**

1. Get RabbitMQ username

```
echo $(kubectl get secret queue-db-default-user -n microservices -o jsonpath='{.data.username}' | base64 --decode)
```

2. Get RabbitMQ password

```
echo $(kubectl get secret queue-db-default-user -n microservices -o jsonpath='{.data.password}' | base64 --decode)
```

3. Get Kong db password

```


echo $(kubectl get secret --namespace "kong" kong-postgresql -o jsonpath="{.data.password}" | base64 --decode)
```
