'''
Rocks wins againist scissors.
Scissors wins against paper.
Paper wins against rock.
'''
import random 
rock= '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper='''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors= '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_images= [rock, paper, scissors]

print('''
    Welcome to Rock, Paper, Scissors!

     🪨         ✂️          📄
    Rock  vs  Scissors  vs  Paper
      ''')

user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for scissors.\n"))
computer_choice= random.randint(0,2)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(f"You chose\n{game_images[user_choice]}\nComputer chose:\n{game_images[computer_choice]}\n")

    if user_choice == computer_choice :
        print("It's a draw, no winner")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win! 🎉")
    else:
        print("You lose! 😢")


