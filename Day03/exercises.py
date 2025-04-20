'''
write a program that works out whether if a given number is an odd or even number
'''

number= int(input("Enter the number: "))
if number % 2 ==0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")


'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight 
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
• Above 35 they are clinically obese.
'''

height= float(input("Enter your height in m: "))
weight= float(input("Enter your weight in kg: "))
BMI= round(weight / height**2, 2) 

if BMI < 18.5:
    print(f"Your BMI is {BMI}, You are Underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, You have normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, You are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, You are obese")
else:
    print(f"Your BMI is {BMI}, You are clinically obese.")


'''
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in
February. The reason why we have leap years is really fascinating.
This is how you work out whether if a particular year is a leap year.
⚫ on every year that is divisible by 4 with no remainder
⚫ except every year that is evenly divisible by 100 with no remainder
⚫ unless the year is also divisible by 400 with no remainder
''' 

year= int(input("Enter the year: "))

if year % 4 == 0 :
    if year % 100 ==0 :
        if year % 400 ==0:
            print(f" Year {year} is leep year.")
        else:
            print(f"Year {year} is a normal year.")
    else:
        print(f" Year {year} is leep year.")
else :
    print(f"Year {year} is a normal year.")
   

'''
Congratulations, you've got a job at Python Pizza! Your first job is to build
an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
D
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
'''
print("Thank you for choosing python pizza Delivaries!")
size= input(f"What size of pizza do you want? S, M, or L? ")
add_pepperoni= input(f"Do you want pepperoni? Y or N? ")
extra_cheese= input(f"Do you want extra cheese? Y or N? ")

bill =0
if size == 'S':
    bill += 15
    if add_pepperoni =='Y':
        bill += 2
elif size=='M':
    bill += 20
    if add_pepperoni =='Y':
        bill += 3
elif size == 'L':
    bill+= 25
    if add_pepperoni =='Y':
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}")


'''
You are going to write a program that tests the compatibility betwee people.
To work out the love score between two people:
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
2. Then check for the number of times the letters in the word LOVE occurs.
3. Then combine these numbers to make a 2 digit number. 
For Love Scores less than 10 or greater than 90, 
the message shoul "Your score is *x*, you go together like coke 
and For Love Scores between 40 and 50, the message should be:
"Your score is *y*, you are alright together." 
Otherwise, the message will just be their score. e.g.:
"Your score is *z*."
'''

print("The love calculator is calculating your score...")
name1= input("What's your name? ")
name2= input("What is their name? ")
combined_names= (name1 + name2).lower()
digit1=0
digit2=0

for i in range (len(combined_names)):
    if combined_names[i] in "true":
        digit1 += 1
    if combined_names[i] in "love":
        digit2 += 1

score= int(str(digit1)+str(digit2))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")




