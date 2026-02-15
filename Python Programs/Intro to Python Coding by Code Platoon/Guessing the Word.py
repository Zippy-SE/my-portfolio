secret_word = "python"
guess = ""
attempts = 0
max_attempts = 3

print("Guess the secret word!")

while guess != secret_word and attempts < max_attempts:
    guess = input("your guess: ")
    attempts += 1
    if guess != secret_word:
        print("Wrong guess. Try again!")    
if guess == secret_word:
    print("Congratulations! You guessed the secret word.")
else:
    print("Sorry, you've used all your attempts. Better luck next time!")   