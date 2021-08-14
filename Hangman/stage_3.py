import random
guess_word = ['python', 'java', 'kotlin', 'javascript']
pick_word = random.choice(guess_word)
print("H A N G M A N")
word = input("Guess the word: ")
if word == pick_word:
    print("You survived!")
else:
    print("You lost!")