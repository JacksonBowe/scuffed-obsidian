## These docs

Make them look nicer
See pull request: https://github.com/ppeetteerrs/obsidian-zola/issues/41
And resource: https://visjs.github.io/vis-network/docs/network/nodes.html 

## Login

* [ ] All buttons should be disabled while login is attempting

## Chat

* [ ] When user sends chat message it should auto append to messages list locally
* [ ] Arriving IoT messages from the current user should be filtered and not added to the current messages list
* [ ] Chat should send with current user's username
* [ ] Lobby and Private chats don't work because user is not subscribed to them. Need to fix. User can be subscribed to all chat messages? Yes user should be subscribed to all otherwise they can miss private messages
* [ ] Text inside chatbox colour should represent target
* [ ] If user is not in LOBBY, should not be able to send lobby messages
* [ ] When private message, how to specify target

## Roles

* [ ] Create role json structure
* [ ] Python script to convert roles.json into markdown?
* [ ] 

When getting the players in a lobby, possibly don't want to return complete user data. Just the data relevant to the lobby. Unsure

## Engine

* [x] User specifies what "role tags" they want to be in the game, select roles based on the tags provided
* [x] Assign roles to players
* [x] For each player import required role
* [x] Contruct a GameState
* [x] Export the GameState
