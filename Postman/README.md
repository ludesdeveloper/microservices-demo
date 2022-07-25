# Testing

### **Prequisites**

1. Import Microservices Demo.postman_collection.json to your Postman
2. Make sure you change ip address
   ![nip-ip-address](pic/nip-ip-address.png)

### **How To**

1. Create new user (consumer)
   ![create-consumer](pic/create-consumer.png)
   ![create-consumer-konga](pic/create-consumer-konga.png)
2. Login and get jwt
   ![get-jwt](pic/get-jwt.png)
3. Write to database to without bearer token
   ![post-without-token](pic/post-without-token.png)
4. Write to database with bearer token
   ![post-with-token](pic/post-with-token.png)
   ![check-db](pic/check-db.png)
