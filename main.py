
import random

words = ["python", "computer", "internship", "programming", "developer"]
word = random.choice(words)
guessed = []
wrong = 0
max_wrong = 6

print("Welcome to Hangman!")
print("Guess the hidden word one letter at a time.")

while wrong < max_wrong:
    display = " ".join(letter if letter in guessed else "_" for letter in word)
    print("\nWord:", display)
    print("Incorrect guesses:", wrong, "/", max_wrong)

    if all(letter in guessed for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Enter one letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one valid letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong += 1
        print("Wrong guess!")

else:
    print("\nGame over! The word was:", word)

if all(letter in guessed for letter in word):
    print("Final Result: WIN")
