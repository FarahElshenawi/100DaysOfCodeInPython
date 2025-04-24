'''
Write a program that calculates the average student height from a list of heights.
Without using len() or sum()
'''

student_heights= input("Enter student heights separated with space\n").split()

for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])

height_sum= 0
student_num= 0
for i in range (len(student_heights)):
    student_num+=1
    height_sum += student_heights[i]

average_height= round(height_sum / student_num)
print(f"Total height = {height_sum}\nNumber of students = {student_num}\nAverage height = {average_height}")


'''
Write a program that calculates the heights score from a list of score
Don't use max() or min() functions.
'''
student_scores= input("Enter student scores separated by space.\n").split()
for i in range(len(student_scores)):
    student_scores[i] = int(student_scores[i])

max_score=0
for i in range(len(student_scores)):
    if student_scores[i] > max_score :
        max_score = student_scores[i]
print(f"The highest score in the class is: {max_score}")

'''
Write a program that calculates the sum of all the even numbers from 1 to X.
If X is 100 then the first evennumber would be 2 and the last one is 100
'''

target= int(input("Enter a number between 0 and 1000\n"))
result=0
for i in range(target+1):
    if i % 2 ==0:
        result += i 
print(result)

'''
Another simple solution
'''
target= int(input("Enter a number between 0 and 1000\n"))
result=0
for i in range(0, target + 1, 2):
    result += i
print(result)


'''
You are going to write a program that automatically prints the solution to the FizzBuzz game. 
These are the rules of the FizzBuzz game:
Your program should print each number from 1 to 100 in turn and include number 100.
When the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz"."
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''

for i in range(1, 101):
    if i % 5 ==0 and i % 3 ==0 :
        print("FizzBuzz")
    elif i % 3 ==0 :
        print("Fizz")
    elif i % 5 ==0 :
        print("Buzz")
    else:
        print(i)


