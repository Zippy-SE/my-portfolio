secret_word = "python"
guess = ""

print("Guess the secret word!")

while guess != secret_word:
    guess = input("your guess: ")

print("Congratulations! You guessed the secret word.")