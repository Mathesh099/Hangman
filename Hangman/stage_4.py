import random
guess_word = ['python', 'java', 'kotlin', 'javascript']
pick_word = random.choice(guess_word)
print("H A N G M A N")
store_word = []
for i in range(len(pick_word)):
    if i < 3:
        store_word.append(pick_word[i])
    else:
       store_word.append('-')
stored_word = "".join(store_word)
word = input(f"Guess the word {stored_word}: ")
if word == pick_word:
    print("You survived!")
else:
    print("You lost!")