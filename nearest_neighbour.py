import random

def find_any(pattern, phrases):
    found = {}
    prev = ''
    ignore = ['the','be','to','of','and','a','in','that','have','i','it','for','not','on','with','he','as','you','do','at','this','but','his','by','from','they','we','say','her','she','or','an','will','my','one','all','would','there','their','what','so','up','out','if','about','who','get','which','go','me','when','make','can','like','time','no','just','him','know','take','person','into','year','your','good','some','could','them','see','other','than','then','now','look','only','come','its','over','think','also','back','after','use','two','how','our','work','first','well','way','even','new','want','because','any','these','give','day','most','us']
    clean_pattern = clean_words(pattern)
    for phrase in phrases:
        clean_prev = clean_words(prev)
        shared_words = set(clean_pattern) & set(clean_prev)
        non_meaningful = set(shared_words) & set(ignore)
        too_many = max(len(clean_prev) - len(clean_pattern) - len(non_meaningful),0)
        similarity_score = len(shared_words) - len(non_meaningful) - too_many * 0.1
        if similarity_score in found:
            found[similarity_score].append((prev,phrase))
        else:
            found[similarity_score] = [(prev,phrase)]
        prev = phrase
    return found

def clean_word(word):
    word_clean = ''
    for letter in list(word):
        if letter.isalpha():
            word_clean += letter.lower()
    return word_clean

def clean_words(phrase):
    words = []
    for word in phrase.split():
        words.append(clean_word(word))
    return words

def flesh_out(partial_question, prev_phrase):
    x = clean_word(partial_question)
    if (x == 'how') or (x == 'who') or (x == 'what') or (x == 'where') or (x == 'when') or (x == 'why'):
        partial_question += " " + prev_phrase
    return partial_question

def chat(database = 'funny_dataset.txt', debug = False):
    with open(database) as f:
        content = f.readlines()
    question, reply = '', ''

    while True:
        question = input("\n user > ")
        print
        if question == 'bye':
            print("\n computer > take care")
            break 
        question = flesh_out(question, reply)
        partial_matches = find_any(question, content)
        best_matches = partial_matches[max(partial_matches.keys())]
        chosen_match, reply = random.choice(best_matches)
        if debug: print ("\n reminds me of:",[chosen_match])
        print("\n computer >",reply) 

chat(database = "funny_dataset.txt")
