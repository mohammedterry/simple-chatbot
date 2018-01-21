import random

intents = {"hi": "hello/hi/heya/hiya/howdy/heyho/whats up?/how are you?".split("/"),
    "bye":"goodbye/bye/bye bye/ciao/see you/laters/adios".split("/"),
    "confused":"??/what do you mean?/i dont get it?/huh?/what?/sorry?/excuse me?/i beg your pardon?/come again?/i dont understand".split("/"),
    "rude":"go away/i hate you/you are so annoying/be quiet".split("/"),
    "angry":"grrr/hey! thats not nice/you're so rude/someone's touchy!/goodness me!/what's wrong with you!".split("/")}

responses = {"hi":"hi",
    "bye":"bye",
    "rude":"angry",
    "angry":"rude",
    "unknown phrase":"confused"}

known_phrases = {phrase:intent for intent in intents.keys() for phrase in intents[intent]}

intent = "hi there"
print(intent)
while intent != "bye":
    phrase = input("> ")
    if phrase in known_phrases:
        intent = known_phrases[phrase]
    else:
        intent = "unknown phrase"
    reply = random.choice(intents[responses[intent]])
    print(reply)
