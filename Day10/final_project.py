'''calculator'''
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def devide(n1, n2):
    return n1 / n2

operations= {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide
}

def calculator():
    num1= float(input("What's the first number? "))
    for sympol in operations:
        print(sympol)
    should_continue= True

    while should_continue:
        operational_sympol= input('Pick an operation: ')
        num2= float(input("What's the next number? "))
        calculation_function= operations[operational_sympol]
        answer= calculation_function(num1, num2)

        print(f"{num1} {operational_sympol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: " ) == 'y':
            num1= answer
        else:
            clear()
            calculator()

calculator()