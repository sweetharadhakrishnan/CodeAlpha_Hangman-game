import random

def hangman():
    words = ["apple", "banana", "cherry", "orange", "grapes"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word.strip())

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word correctly.")
            break
    else:
        print(f"Game Over! The word was: {word}")

hangman()
