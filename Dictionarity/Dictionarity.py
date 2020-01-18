text = """
   ____/ /(_)_____ / /_ (_)____   ____   ____ _ _____ (_)/ /_ __  __
 / __  // // ___// __// // __ \ / __ \ / __ `// ___// // __// / / /
/ /_/ // // /__ / /_ / // /_/ // / / // /_/ // /   / // /_ / /_/ / 
\__,_//_/ \___/ \__//_/ \____//_/ /_/ \__,_//_/   /_/ \__/ \__, /  
                                                          /____/ 
"""

import json
from difflib import get_close_matches

print(text)
data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(w, data.keys())[0]} instead? [Y/N]: ")
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter a word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

