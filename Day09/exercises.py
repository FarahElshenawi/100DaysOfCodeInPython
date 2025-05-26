'''
1- write a program that converts their scores to grades.
By the end of the program you should have new dictionary called student_grades{name: grade}
'''
student_scores={
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Darco": 74,
    "Neville": 62
}     
student_grades= {}
for key in student_scores:
    if student_scores[key] > 90 :
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectation"
    elif student_scores[key] > 70 :
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)

'''
2- write a program that adds to a travel_log.
'''
travel_log=[
{
    "country": 'France',
    "visits": 12,
    'cities': ["Paris", "Lille", "Dijon"] 
},
{
    "country": "Germany",
    "visits": 5,
    'cities': ["Berlin", "Hamburg", "Stuttgart"]
}
]

def add_new_country(country_visited:str, time_visited:int, cities_visited:list):
    travel_log.append(
        {
            "country": country_visited,
            "visits": time_visited,
            "cities": cities_visited
        }
    )

add_new_country("Russia", 2, ["Moscow", "Saint Petersbu"])
print(travel_log)
