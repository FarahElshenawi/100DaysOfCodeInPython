# PyPassword Generator
import random

print("Welcome to the pypassword Generator!")

letters=  [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
digits = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
symbols = [ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
            '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
            ':', ';', '"', "'", '<', '>', ',', '.', '?', '/' ]

letters_no= int(input("How many letters would you like in your password?\n"))
sympols_no= int(input("How many sympols wouuld you like?\n"))
numbers_no= int(input("How many numbers would you like?\n"))

pass_letters= random.choices(letters, k= letters_no)
pass_digits= random.choices(digits, k=numbers_no)
pass_sympols= random.choices(symbols, k= sympols_no)

password= pass_digits + pass_letters + pass_sympols
random.shuffle(password)
password = "".join(password)
print(f"Here is your password: {password}")
 

'''
Sure this is not the expected code to be a final project for a day of loops in python so I will think of another way
'''
import random

print("Welcome to the pypassword Generator!")

letters=  [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
digits = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
symbols = [ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
            '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
            ':', ';', '"', "'", '<', '>', ',', '.', '?', '/' ]

letters_no= int(input("How many letters would you like in your password?\n"))
sympols_no= int(input("How many sympols wouuld you like?\n"))
numbers_no= int(input("How many numbers would you like?\n"))

if not letters_no.isdigit() or not sympols_no.isdigit() or not nr_numbers.isdigit():
  print("Invalid value, enter a number instead.")
else:
  password = []

  random_letter = random.randint(0, 51)
  for i in range(0, letters_no):
    random_letter = random.randint(0, 51)
    password.append(letters[random_letter])

  random_number = random.randint(0,9)
  for i in range(0, numbers_no):
    random_number = random.randint(0,9)
    password.append(digits[random_number])

  random_symbol = random.randint(0,8)
  for i in range(0, sympols_no):
    random_symbol = random.randint(0,8)
    password.append(symbols[random_symbol])

  random.shuffle(password)
  print(f"Here is your password: {''.join(password)}")

  if len(password) <= 6:
    print("Your password is weak, try to include at least 8 characters for a stronger password.")
  elif len(password) == 7:
    print("Your password is medium, try to include at least 8 characters for a stronger password.")
  else:
    print("Your password is strong.")