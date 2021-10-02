import random
import string
guess_word = ['python', 'java', 'kotlin', 'javascript']
pick_word = random.choice(guess_word)
print("H A N G M A N")
length = len(pick_word)
store_word = "-" * length
chars = []

x = 8
while x > 0:
    stored_word = "".join(store_word)
    if '-' not in stored_word:
        break

    else:
        print()
        print(stored_word)
    
        check_word = input("Input a letter: ")
    
        if len(check_word) != 1:
            print("You should input a single letter")
        elif check_word not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
        elif check_word in chars:
            print("You've already guessed this letter")
        elif check_word not in pick_word:
            print("That letter doesn't appear in the word")
            x -= 1
        elif check_word in pick_word:
            for n in range(len(pick_word)):
                if check_word == pick_word[n]:
                    store_word = store_word[:n] + check_word + store_word[n + 1:]
    chars.append(check_word)

if x < 0:
    print("You lost!")
else:
    print("You guessed the word ",pick_word,"!")
    print("You survived!")
