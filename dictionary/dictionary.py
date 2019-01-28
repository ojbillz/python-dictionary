import json
from difflib import get_close_matches


dictionary = json.load(open("dictionary.json"))


def definition(word):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    elif word.title() in dictionary:
        return dictionary[word.title()]
    elif word.upper() in dictionary:
        return dictionary[word.upper()]
    elif len(get_close_matches(word, dictionary.keys())) > 0:
        yesno = input("Did you mean %s? Please use N for No and Y for Yes " % get_close_matches(word, dictionary.keys())[0])
        if yesno == "Y":
            return dictionary[get_close_matches(word, dictionary.keys())[0]]
        elif yesno == "N":
            return "Please re enter your word."
        else:
            return "Your entry is not understood, please try again."
    else:
        return("I don't understand what you mean. Please repeat. ")

returnedWord = input("What did you want to find out the definition for? ")
word = definition(returnedWord)
result = definition(returnedWord)
result = str(result).replace("[", " ").replace("'", " ").replace("]", " ").replace(" \" ", " ").replace("]", " ")

if type(result) == list:
    for item in output:
        print("~", result)
else:
    print("~", result)




