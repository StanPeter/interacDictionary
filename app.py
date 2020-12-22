import json
import emoji
from difflib import get_close_matches


# database for the project
data = json.load(open("data.json", "r"))
word_list = tuple(data.keys())


# go through the database and find all matches of the input
def translator(word):
    if word in data:  # for words like NASA
        w = word
    elif word.capitalize() in data:  # for words like Dublin
        w = word.capitalize()
    else:
        w = word.lower()  # for mistakes 'River' instead of 'river'

    similar_word = get_close_matches(w, word_list, n=1, cutoff=0.7)

    while True:
        if w in data:
            return word_printer(w)

        elif similar_word:  # if the word was badly spelled, example: 'rivver'
            answer = input(
                f"Your word wasn't found, did you mean '{similar_word}' instead?  y / n \n")
            if answer == "y":
                return translator(similar_word[0])
            elif answer == "n":
                return "You quit the programme"
            else:
                return print("Your response has to be 'y' or 'n', please repeat")

        else:
            return "Unfortunately your word was not found in my dictionary, please check again if its correct"


# print the final output of the found word
def word_printer(word):
    print("\n \n")

    for phrase in data[word]:
        print(phrase + "\n")

    print("\n")


# clearer communication in Terminal
def user_interface():
    print("Hello, my name is Bob and I will be your assistant throughout this translator")

    word = input("Please tell me the word you wish to find \n\n")

    # repeat the programme until the user wishes
    while True:
        translator(word)

        word = input(
            "Please tell me the word you wish to find, to end the programme press 'q'   \n\n")
        if word == "q":
            print(emoji.emojize("Thank you for your time :thumbs_up:"))
            break


user_interface()
