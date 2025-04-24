# Hangman Game
import random

def replace_char(string, index, new_char):
    return string[:index] + new_char + string[index+1:]

# ASCII stages
stages = [
    '''
     _______
    |       |
    |       
    |      
    |      
    |      
    |      
    |______
    ''',
    '''
     _______
    |       |
    |       O
    |      
    |      
    |      
    |      
    |______
    ''',
    '''
     _______
    |       |
    |       O
    |       |
    |      
    |      
    |      
    |______
    ''',
    '''
     _______
    |       |
    |       O
    |      /|
    |      
    |      
    |      
    |______
    ''',
    '''
     _______
    |       |
    |       O
    |      /|\\
    |      
    |      
    |      
    |______
    ''',
    '''
     _______
    |       |
    |       O
    |      /|\\
    |      / 
    |      
    |      
    |______
    ''',
    '''
     _______
    |       |
    |       O
    |      /|\\
    |      / \\
    |      
    |      
    |______
    '''
]

words = [
    # Short and long words mixed
    "cat", "dog", "pen", "tree", "lamp", "moon", "chair", "apple", "house", "cloud", "grape", "radio", "blanket",
    "rocket", "orange", "camera", "journey", "fashion", "cherry", "capture", "rainbow", "hospital", "vacation",
    "mountain", "universe", "strategy", "snowflake", "breakfast", "incredible", "lighthouse", "celebration",
    "congratulate", "firefighters", "misunderstand", "transportation", "thankfulness"
]

def play_game():
    random_word = random.choice(words)
    blanks = '_' * len(random_word)
    guessed_letters = set()
    lives = 6
    stage = 0

    print("\nWelcome to Hangman!\n")
    print(blanks + "\n")
    print(stages[stage])

    while lives > 0:
        letter = input("Guess a letter: ").lower()

        # Validate input
        if not letter.isalpha() or len(letter) != 1:
            print("Please enter a single alphabetic character.\n")
            continue

        # Repeated guess
        if letter in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        guessed_letters.add(letter)

        # Correct guess
        if letter in random_word:
            for i, char in enumerate(random_word):
                if char == letter:
                    blanks = replace_char(blanks, i, letter)
            print(f"Good guess!\n{blanks}\n")

            if "_" not in blanks:
                print("🎉 YOU WIN! 🎉\n")
                break
        else:
            lives -= 1
            stage += 1
            print(f"You guessed '{letter}', that's not in the word. You lost a life.")
            print(stages[stage])
            print(f"Word: {blanks}")
            print(f"Lives left: {lives}\n")
    
    if "_" in blanks:
        print(f"💀 You lose! The word was: {random_word} 💀\n")

    # Play again?
    again = input("Play again? (y/n): ").lower()
    if again == 'y':
        play_game()
    else:
        print("Thanks for playing! 🌟")

# Run the game
play_game()
