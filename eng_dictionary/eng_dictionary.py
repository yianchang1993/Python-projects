import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean % s instead? Enter Y if yes, N for no: " %
                   get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        if yn == "N":
            return "The word doesn't exit, please double check again!"
        else:
            return "error input"
    else:
        return "The word doesn't exit, please double check again!"


word = input("Enter word:")
output = translate(word)
if isinstance(output, list):
    for item in output:
        print(item)
    else:
        print(output)
