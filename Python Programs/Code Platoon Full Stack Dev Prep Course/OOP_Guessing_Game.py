import random

class GuessingGame:
    def __init__(self, answer):
        self.answer = answer
        self.last_guess = None

    def guess(self, user_guess):
        user_guess = int(user_guess)
        self.last_guess = user_guess
        if user_guess > self.answer:
            return 'high'
        elif user_guess == self.answer:
            return 'correct'
        else:
            return 'low'

    def solved(self):
        return self.last_guess == self.answer
    
game = GuessingGame(random.randint(1, 100))
last_guess  = None
last_result = None

while not game.solved():
    if last_guess is not None:
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
        print()

    last_guess  = input("Enter your guess: ")
    last_result = game.guess(last_guess)

print(f"{last_guess} was correct!")