import random
guess_word = ['python', 'java', 'kotlin', 'javascript']
pick_word = random.choice(guess_word)
print("H A N G M A N")
store_word = []

for i in range(len(pick_word)):
    store_word.append('-')

x = 8
while x > 0:
    stored_word = "".join(store_word)
    print()
    print(stored_word)

    if '-' not in stored_word:
        break

    check_word = input("Input a letter: ")

    if check_word in stored_word:
        print("No improvements")
        x -= 1
    if check_word not in pick_word:
        print("That letter doesn't appear in the word")
        x -= 1
    elif check_word in pick_word:
        for n in range(len(pick_word)):
            if check_word == pick_word[n]:
                store_word[n] = pick_word[n]

if x == 0:
    print("You lost!")
else:
    print("""You guessed the word!
You survived!""")
