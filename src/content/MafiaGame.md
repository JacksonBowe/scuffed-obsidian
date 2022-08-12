# Mafia Overview

See what I'm working on: *TODO's*

### What is this?

Mafia is a *Serverless* *Social Deduction Game* that I'm making using *Amazon Web Services* in my spare time. It uses a number of different amazon services and follows common *Serverless Design Patterns* to fit the serverless mould - while also being a fully functional *Web Based Game*.

### Mechanics

The game isn't strictly turn based however it follows a similar principle in that there are two main states, Day and Night. 

During the Day all members of the town (inclusive of the mafia members) gather to discuss what leads they have found on the Mafia. At this time they may also decide to remove a player under suspicion of being a member of the Mafia.

During the Night, the Mafia collude to kill off a member of the Town. Also, certain members of the Town can perform actions like "Follow target player tonight" or "Inspect role" etc.

### Tools I'm using to make this

##### *Backend*

* [AWS ApiGateway](https://aws.amazon.com/api-gateway/) for the API layer
* [AWS DynamoDB](https://aws.amazon.com/dynamodb/) as a database following [Single Table Design](https://aws.amazon.com/blogs/compute/creating-a-single-table-design-with-amazon-dynamodb/) principles
* [AWS Cognito](https://aws.amazon.com/cognito/) for user authentication
* [AWS S3](https://aws.amazon.com/s3/) for medium/large file storage (images etc)
* [AWS IoT Core](https://aws.amazon.com/iot/) for the pub/sub functionality
* [Postman](https://www.postman.com/) to test and document the API

##### *Frontend*

Open disclaimer: I am not a front end developer. I'm not even a backend developer come to think of it.

Currently I'm making the front end with [Quasar Framework](https://quasar.dev/) - a Vue.js wrapper. It seems like a good idea based on my skill level right now. I don't know a whole lot of Javascript or Vue, or anything about web development (but how hard can it be?).

Main reason I'm using Quasar is because it comes with a bunch of prebuild components and really easy to follow documentation. It also lets me use the same codebase to deploy to the web and a standalone executable. This sparks joy.

##### *The glue*

I've named the individual backend services and frontend framework, but they're essentially useless without a way to seamlessly integrate them together. That's where [Serverless Stack (SST)](https://serverless-stack.com/) comes in.

SST is a cloud architecture development kit that lets you provision AWS Infrastructure as Code (IaC) by leveraging the base [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) with improvements geared towards serverless applications. 

If you've used any IaS providers in the past like eTerraform, AWS CDK, Serverless, SAM etc I seriously recommend checking out SST. It's next level.

### Objectives

* Serverless (Because it's fun and hopefully cheaper)
* Deployed to web
* Deployed to desktop application
* ???
* Profit?

\#mafia-sdg #serverless #sst #todo
