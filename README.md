# **DEMO MICROSERVICES**

<p align="center">
<img src="pic/ludes.png" width="500">
</p>

### **Tech Stack**

1. Kubernetes
2. Kong
3. Konga
4. Rabbit MQ

### **Diagram**

![microsevices-demo-diagram](pic/microsevices-demo-diagram.png)

### **Deployment**

1. Please refer to this [Deployment](Kubernetes-Manifests/) folder

### **Postman Testing**

1. Please refer to this [Postman](Postman/) folder

### **Microservices**

1. [Register Consumer](Register-Consumer/). Register consumers to Kong DB
2. [Login Consumer](Login-Consumer/). Get secret + key from Kong Admin, craft jwt, and send back to client
3. [Get Request](Get-Request/). Receive request from client and publish to RabbitMQ
4. [Write Database](Write-Database/). Subscribe new message from RabbitMQ and write to DB

### **Screenshot**

1. Konga to Kong configuration
   > ![konga-to-kong-config](pic/konga-to-kong-config.png)
2. Kong ingress controller manage by Konga
   ![kong-ingress-controller-manage-by-konga](pic/kong-ingress-controller-manage-by-konga.png)
3. RabbitMQ dashboard
   ![rabbitmq-dashboard](pic/rabbitmq-dashboard.png)
4. K9S port forward
   ![k9s-port-forward](pic/k9s-port-forward.png)
