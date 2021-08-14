import random
guess_word = ['python', 'java', 'kotlin', 'javascript']
pick_word = random.choice(guess_word)
print("H A N G M A N")
store_word = []

for i in range(len(pick_word)):
    store_word.append('-')

for i in range(8):
    stored_word = "".join(store_word)
    print()
    print(stored_word)
    check_word = input("Input a letter: ")
    if check_word not in pick_word:
        print("That letter doesn't appear in the word")
    elif check_word in pick_word:
        for n in range(len(pick_word)):
            if check_word == pick_word[n]:
                store_word[n] = check_word

print()
print("""Thanks for playing!
We'll see how well you did in the next stage
""")
