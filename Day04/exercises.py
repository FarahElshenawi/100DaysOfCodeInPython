'''
Write a virtual coin toss program. It will randomly tell the user "head" or "tail"
'''
import random

print("Start the game")

# Ask the user if they want to flip
flip = int(input("Flip or not? (1 = Yes, 0 = No): "))

while flip == 1:
    random_int = random.randint(0, 1)
    if random_int == 0:
        print("Head")
    else:
        print("Tail")
    
    # Ask again after the flip
    flip = int(input("Flip again? (1 = Yes, 0 = No): "))

print("Game Over")


'''
Write a program that will select a random name from a list of numbers. 
The person selected will have to pay for everybody's food bill
'''
names= input("Please enter your names separated by ', ': ")
names = names.split(', ')
random_index= random.randint(0, len(names)-1)

print(f"{names[random_index]} is going to buy the meal today!")


'''
Write a program that will mark a spot on a map with an x. 
    A   B   C                         A   B   C
  +---+---+---+                     +---+---+---+
1 |   |   |   |                   1 |   |   |   |
  +---+---+---+        C2           +---+---+---+
2 |   |   |   |     ---------->   2 |   |   | X |
  +---+---+---+                     +---+---+---+
3 |   |   |   |                   3 |   |   |   |
  +---+---+---+                     +---+---+---+
 
'''
line1= ["","",""]
line2= ["","",""]
line3= ["","",""]
map= [line1, line2, line3] 

print("Hiding your treasure! X marks the spot.")
position= input("Where do you want to put the treasure? ")
i=0
j=0
if position[1] in'123':
    i = int(position[1])-1
if position[0] =='A':
    j = 0
elif position[0] == 'B':
    j=1
else:
    j=2

map[i][j]='X'
print(f"{line1}\n{line2}\n{line3}")

'''
Another solution
'''
line1= ["","",""]
line2= ["","",""]
line3= ["","",""]
map= [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position= input("Where do you want to put the treasure? ")

letter= position[0].lower()
abc=['a','b','c']
letter_index= abc.index(letter)
number_index= int(position[1])-1
map[number_index][letter_index]= 'X'

print(f"{line1}\n{line2}\n{line3}")
