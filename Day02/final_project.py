'''
Tip Calculator
'''

print("Welcome to the Tip Calculator!")
total_pill= float(input("What was the total pill? $"))
tip= int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people= int(input("How many people to split the bill? "))

aLL_cost= total_pill + total_pill* (tip/100)
cost_per_person= round(aLL_cost / no_of_people, 2)

print(f"Each person should pay: ${cost_per_person}")
