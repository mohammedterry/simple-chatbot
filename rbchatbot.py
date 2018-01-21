intentions = { "hello": "hello",
   "hi": "hello",
   "hiya": "hello",
   "howdy": "hello",
   "hey": "hello",
   "heya":"hello",
   "goodbye":"goodbye",
   "bye": "goodbye",
   "ciao":"goodbye",
   "see you":"goodbye",
   "go away":"goodbye"}
responses = {"hello": "how are you?",
    "help":"how exactly can i help?",
    "goodbye":"take care"}

reply = ""
while reply != "take care":
phrase = input("> ")
if phrase in intentions:
reply = responses[intentions[phrase]]
print(reply)
else:
print("sorry i dont know what you mean?")

