# Controllers

### What is this

Controllers are what I use to refer to the different branches in the microservice approach I'm using to create [MafiaGame](#/content/MafiaGame.md)

#### Currently implemented

* [AuthController](#/content/Technical/AuthController.md) - handles registration/login/recovery/etc
* *ChatController* - handles chat messages broadcast/lobby/private/etc

##### Todos

* *GameController*?
* [LobbyControllerTasks](#/content/Misc/LobbyControllerTasks.md)
* *UserController*
* Others probably

#### Controller Template

````ad-note
title: Python template
collapse: close
~~~python
import json

cors_headers = {
'Content-Type': 'application/json',
'Access-Control-Allow-Headers': '*',
'Access-Control-Allow-Credentials': 'true',
'Access-Control-Allow-Origin': 'http://localhost:8080',
'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
}

def fail(msg):
return {
'statusCode': 403,
'headers': cors_headers,
'body': json.dumps(msg)
}

def success(msg):
return {
'statusCode': 200,
'headers': cors_headers,
'body': json.dumps(msg)
}


def handler(event, context):
print('request: {}'.format(json.dumps(event)))

httpMethod = event['requestContext']['http']['method']
resource = event['requestContext']['http']['path']
request_params = event.get('queryStringParameters', None)
request_body = {}

if 'body' in event and event['body'] != None:
request_body = json.loads(event['body'])

result = {}

if resource == '':
if httpMethod == '':
pass

return {
"statusCode": 200,
"headers": cors_headers,
"body": json.dumps(event)
}
~~~

````

\#technical
