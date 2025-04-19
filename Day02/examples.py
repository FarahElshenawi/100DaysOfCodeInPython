'''
1- Write a program that add the digits in a 2 digit number
'''
two_digit_number= input("Enter two digit numbers ")
print(type(two_digit_number))
first= int(two_digit_number[0])
second= int(two_digit_number[1])
print(first+second)

'''
2- write a program that calculate the Body Mass Index(BMI) from a user's weight and height 
BMI= Weight(kg) / height^2 (m^2) 
'''
height= float(input("Enter your height in m: "))
weight= float(input("Enter your weight in kg: "))
BMI= weight / height**2 
print(round(BMI, 2)) 

'''
3- write a program using math and f-string that tells us 
how many weeks we have left, if we will live until 90 years old
'''
current_age= int(input("Please Enter your current age: "))
weeks_per_year= round(365/7)
years_left= 90 - current_age
weeks_left= years_left * weeks_per_year
print(f"You have {weeks_left} weeks left.")