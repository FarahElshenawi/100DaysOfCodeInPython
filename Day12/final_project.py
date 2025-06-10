import random

class NumberGuessingGame:
    def __init__(self, min_number=1, max_number=100, easy_attempts=10, hard_attempts=5):
        self.min_number = min_number
        self.max_number = max_number
        self.easy_attempts = easy_attempts
        self.hard_attempts = hard_attempts
        self.target_number = None
        self.attempts_left = None
        self.game_won = False

    def setup_game(self):
        print(f"Welcome to the Number Guessing Game!")
        print(f"I'm thinking of a number between {self.min_number} and {self.max_number}.")
        self.target_number = random.randint(self.min_number, self.max_number)
        difficulty = self._get_valid_difficulty()
        self.attempts_left = self.easy_attempts if difficulty == 'easy' else self.hard_attempts

    def _get_valid_difficulty(self):
        while True:
            choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
            if choice in ['easy', 'hard']:
                return choice
            print("Invalid input. Please type 'easy' or 'hard'.")

    def _get_valid_guess(self):
        while True:
            try:
                guess = int(input("Make a guess: "))
                if self.min_number <= guess <= self.max_number:
                    return guess
                print(f"Please enter a number between {self.min_number} and {self.max_number}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_guess(self, guess):
        self.attempts_left -= 1
        if guess == self.target_number:
            print(f"You got it! The answer was {self.target_number}.")
            self.game_won = True
        elif guess > self.target_number:
            print("Too high.")
        else:
            print("Too low.")

    def play(self):
        self.setup_game()
        while self.attempts_left > 0 and not self.game_won:
            print(f"You have {self.attempts_left} attempts remaining to guess the number.")
            guess = self._get_valid_guess()
            self.check_guess(guess)
            if not self.game_won and self.attempts_left > 0:
                print("Guess again.")
        
        if not self.game_won:
            print(f"You've run out of guesses. The number was {self.target_number}. You lose.")
        
        return self._play_again()

    def _play_again(self):
        while True:
            choice = input("Would you like to play again? Type 'yes' or 'no': ").lower()
            if choice in ['yes', 'no']:
                return choice == 'yes'
            print("Invalid input. Please type 'yes' or 'no'.")

def main():
    while True:
        game = NumberGuessingGame()
        play_again = game.play()
        if not play_again:
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()