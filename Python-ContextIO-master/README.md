Context.IO API v2.0 Python Library
==================================

This is the python client library for v2.0 of the Context.IO API!

##Dependencies
RAUTH - If you do not have that, snag it with
```$ pip install rauth```
or 
```$ easy_install rauth```
, or “Use the [Source](https://github.com/litl/rauth), Luke”

REQUESTS - rauth is built on top of the requests module
```$ pip install requests```
or
```$ easy_install requests```
or [Source](https://github.com/kennethreitz/requests)

##Installation
Check out / download the module from git, change directory to the folder with setup.py and run:

    python setup.py install

You'll probably want to toss a sudo before that, depending on your OS. That's it though!

##Usage
You first need to instantiate the main ContextIO object with your API credentials:

	import contextio as c
    
	CONSUMER_KEY = 'YOUR_API_KEY'
	CONSUMER_SECRET = 'YOUR_API_SECRET'
    
	context_io = c.ContextIO(
		consumer_key=CONSUMER_KEY, 
		consumer_secret=CONSUMER_SECRET
	)

The ContextIO class can optionally accept a debug keyword parameter that prints or logs more info about the request and response.

The module is fully docstringed out, so feel free to jump into the python interpreter and help(foo) on stuff. Explore the resource classes and methods!

Here's how you can query the API for an account:

    accounts = context_io.get_accounts(email='johndoe@gmail.com')
    # since we return a list, let's be sure we have a result
    if accounts:
        account = accounts[0]

The Account class has methods to represent all the kinds of requests you can make under that resource.

If you store account ids, message ids, file ids, or anything else like that on your server, you can instantiate these objects without touching the API, for increased speed. Here's an example of how you do that.

	params = {
		'id': 'ACCOUNT_ID_HERE'
	}
	account = c.Account(context_io, params)

That'll just be an empty object, but you need to pass in the "id" since that's used to form the URL for API endpoints for the account resource. If you want to query the API and populate that account object, you can simply do a:

	account.get()

You can use this same technique to populate sub-resource objects too.

	params = {
		'message_id': 'MESSAGE_ID_HERE'
	}
	message = c.Message(account, params)
	# populate the message object with data from the API
	message.get()

Notice how the Message class needs an Account object as a parent? That's because the library uses an object's ancestors to build the URL.

If you have any questions, don't hesitate to contact tony@context.io (that's me!). I'd love to assist you with any issues you encounter and learn how you'll use Context.IO!
