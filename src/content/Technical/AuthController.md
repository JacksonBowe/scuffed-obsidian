# AuthController

### What is this

This is one of the [Controllers](#/content/Technical/Controllers.md) linked to the [Api](#/content/Technical/Api.md) of [MafiaGame](#/content/MafiaGame.md)

#### How am I using it

This controller handles all actions relating to the *AWS Cognito* user pool for the game.  The *UserPool* contains the user accounts, but is only used to authenticate *Users*. 

##### Functions

````ad-success
title: RegisterUser
collapse:true

Payload: 

~~~json
{
	"username": "example@gmail.com",
	"password": "password"
}
~~~

Expected behaviour:

Sends confirmation code to user email


````

````ad-success
title: GetUser
collapse: true

Params:
~~~json
{
	"username": "example@gmail.com"
}
~~~

Expected output: CognitoUserEntity

````

\#technical
