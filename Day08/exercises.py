'''
Area Calculattion  
You are painting a wall. The instructions on the paint can say that 
1 can cover 5 square meters of wall. 
Given a random height and widtth of wall, Calculate how many cans you'ii need to buy. 
'''
import math

def calc_cans(height, width, coverage):
    area= height * width
    num_of_cans= math.ceil(area / coverage)
    return num_of_cans

height= int(input("Enter the height: ")) 
width= int(input("Enter the width: "))
cans= calc_cans(height, width, 5)
print(f"You will need {cans} of cans of paints.")


'''
Prime number checker
'''

def prime_checker(number):
   is_prime= False
   for i in range (2,number):
       if (number % i ==0) :
            is_prime= True
    if is_prime:
       print("prime")
    else:
       print('not prime')
