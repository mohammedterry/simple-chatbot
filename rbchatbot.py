import random

intents = "hello/goodbye/confused".split("/")
hello = "hello/hi/heya/hiya".split("/")
goodbye = "goodbye/bye/ciao/see you/go away".split("/")
confused = "what do you mean?/???/i dont get it?/huh?".split("/")
responses = {"hello": "hello",
    "goodbye":"goodbye"}
intentions = {phrase:intent for intent in intents for phrase in eval(intent)}

reply = ""
while reply != "goodbye":
	phrase = input("> ")
	if phrase in intentions:
		reply = responses[intentions[phrase]]
	else:
		reply = "confused"
	nl_reply = random.choice(eval(reply))
	print(nl_reply)
