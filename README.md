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

1. Please refer to this [deployment](Kubernetes-Manifests/)

### **Microservices**

1. [Register Consumer](Register-Consumer/). Register consumers to Kong DB
2. [Login Consumer](Login-Consumer/). Get secret + key from Kong Admin, craft jwt, and send back to client
3. [Get Request](Get-Request/). Receive request from client and publish to RabbitMQ
4. [Write Database](Write-Database/). Subscribe new message from RabbitMQ and write to DB
