import pandas

#TODO 1. Create a dictionary in this format:
words = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row['letter']: row['code'] for index, row in words.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
isRunning = True
while isRunning:
    user_input = input("What word would you like phonetically?").upper()
    letter_list = [nato_dict[l] for l in user_input]
    print(letter_list)
