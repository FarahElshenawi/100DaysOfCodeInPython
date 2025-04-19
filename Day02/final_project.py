'''
Tip Calculator
'''

print("Welcome to the Tip Calculator!")
total_pill= float(input("What was the total pill? $"))
tip= int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people= int(input("How many people to split the bill? "))

aLL_cost= total_pill + total_pill* (tip/100)
cost_per_person= aLL_cost / no_of_people
final_amount= "{:.2f}".format(cost_per_person)

print(f"Each person should pay: ${final_amount}")
