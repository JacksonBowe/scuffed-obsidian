# HTTP Verb Cheatsheet

### Quick Summary

**<span style="color:orange">POST</span>** - The URI specifies the <span style="color:pink">
*resource*</span> that the supplied entity should be <span style="color:orange">
***created***</span> under

**<span style="color:deepSkyBlue">PUT</span>** - The URI specifies the <span style="color:pink">
*entity*</span> that the supplied data shoud <span style="color:deepSkyBlue">
***replace***</span>

**<span style="color:white">PATCH</span>** - The URI specifies the <span style="color:pink">
*entity*</span> that the supplied data shoud be <span style="color:white">
***merged***</span> with

**<span style="color:greenYellow">GET</span>** - The URI specifies the <span style="color:pink">
*entity*</span> that should be  <span style="color:greenYellow">
***retrieved***</span>  (no body content)

**<span style="color:tomato">DELETE</span>** - The URI specifies the <span style="color:pink">
*entity*</span> that should be  <span style="color:tomato">
***deleted***</span>  (no body content)

### Examples

````ad-warning
title: POST
icon: 
collapse: true


Create item using body data
~~~py
URL = "https://###/api/projects?keys={params}"
BODY = {
	"projectId": "1234-5678-etc",
	"attributes": {
		"projectName": "Example",
		"attribute2": "Value2",
	}
}

RESPONSE = 201 Created
~~~

Note: Any logic handling should be done via the query string params. The `BODY` should exclusively contain the entity that is being created
````

````ad-info
title: PUT
collapse: true

Replace item at {projectId} with body data
~~~py
URL = "https://###/api/projects/{projectId}?keys={params}"
BODY = {
	"projectName": "Example", # If you want to chance name
	"attribute2": "Value2",
}

RESPONSE = 201 Created or 200 OK
~~~

````

````ad-quote
title: PATCH
collapse: true

Modify item at {projectId} with body data (partial update instead of full replace as with PUT)
~~~py
URL = "https://###/api/projects/{projectId}?keys={params}"
BODY = {
	"projectName": "Example", # If you want to chance name
	"attribute2": "Value2",
}

RESPONSE = 201 Created or 200 OK??
~~~

````

````ad-success
title: GET
collapse: true

Get item at {projectId}
~~~py
URL = "https://###/api/projects/{projectId}?keys={params}"
BODY = None

RESPONSE = 200 OK
~~~

OR

Get all projects
~~~py
URL = "https://###/api/projects?keys={params}"
BODY = None

RESPONSE = 200 OK
~~~
````

````ad-error
title: DELETE
collapse: true

Delete item at {projectId}
~~~py
URL = "https://###/api/projects/{projectId}?keys={params}"
BODY = None

RESPONSE = 200 OK

~~~
````

##### Tags

\#serverless #technical
