# Mafia Api

### What is this

*AWS ApiGateway* is Amazons solution for deploying scalable Api endpoints, essentially for free.

#### How am I using it

I'm using ApiGateway as the primary data transfer layer in [MafiaGame](#/content/MafiaGame.md). When *Users* perform actions on the frontend that need to read from either the *AWS DynamoDB* database [Database](#/content/Technical/Database.md) or the *AWS S3* bucket they request the data from the Api, and it handles retrieving it.

I'm setting my Api up with a *Microservice* design. I don't know if this is great practice, it may change in the future. The *Microservice* design means that there's not one big script full of logic that gets executed, but instead smaller more "self-contained" scripts. I label these microservices [Controllers](#/content/Technical/Controllers.md)

The frontend interacts with the API using standard API methods. My understanding, and thus implementation, of these methods is as follows;

````ad-info
title: HTTP Verbs
![[HTTP Verbs#Quick Summary]]
````

*test-folder/t2/t3/t4/Test 1*

##### Controllers

* [AuthController](#/content/Technical/AuthController.md) - handles registration/login/recovery/etc
* *UserController* - handles user actions get/update/etc
* *ChatController* - handles chat messages broadcast/lobby/private/etc

\#technical
