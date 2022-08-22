import random


word_list = ["apple","banana"]
user_word = random.choice(word_list)
user_s = len(user_word)
user_interface = int(user_s) * "_"
stikes = 0
goodwords = list(user_word)
print(user_interface)
print(goodwords)

userguess = input("Guess: ")
if userguess == goodwords:
    print("Good")
#working progress
