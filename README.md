# Telegram Forwarder Bot
### Copy/Paste a channel messages to your channel

<br>
This bot will copy/paste any message that arrives in a channel to your own channel

## Why Copy/Paste messages?
This is useful when:
<li> You want to back up a channel messages</li>
<li> You want to buy a premium channel with your friends, so you can have premium channel messages in your own channel and share it with your friends ( don't do this :) )</li>
<li>You simply want to copy a channel messages to your own with some changes and adding your own signature</li>
<li> etc. ...</li>

## Futures
<li>Copy/Paste messages</li>
<li>Filter words</li>
<li>Adding signature</li>

## Installation
1 - Install requirements from `requirements.txt`

2 - Add your `API_ID`, `API_HASH` and `sudo IDs` to `/plugins/jsons/config.json`

3 - Run `main.py`

4 - Enter your credentials and login

5 - Done

## Commands
This bot will only answer to `itself` and `sudos`

| Command 	| Description 	| Examples 	|
|---	|---	|---	|
| add channel [base] to [target] 	| Link "base" channel to "target" channel 	| - add channel @durov to @username<br>- add channel -100123456 to -100654321 	|
| remove channel [base] 	| Unlink "base" channel from all target channels 	| - remove channel @durov<br>- remove channel -100123456 	|
| add filter "[base]" to "[target]" 	| Filter "base" word to "target" word 	| - add filter "hello" to "bye"<br>- add filter "me" to "you" 	|
| remove filter "[base]" 	| Remove all filters of "base" word 	| - remove filter "hello" 	|
| sign text [text] 	| Update sign text to [text] 	| - sign text Join my channel @username 	|
| filters 	| Show all filters 	|  	|
| channels 	| Show all linked channels 	|  	|
| settings 	| Show all settings 	|  	|
| on \| off 	| Turn bot on or off 	| - on<br>- off 	|
| filters [ on \| off ] 	| Enable/Disable filtering words 	| - filters on<br>- filters off 	|
| sign [ on \| off ] 	| Enable/Disable adding signature 	| - sign on<br>- sign off 	|
| help 	| Show this table as a message 	|  	|

---

Support: [Join Group](https://t.me/PythonUnion)
