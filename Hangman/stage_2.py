guess_word = ['python']

print("H A N G M A N")
word = input("Guess the word: ")
if word in guess_word:
    print("You survived!")
else:
    print("You lost!")