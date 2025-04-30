'''You will find the solution from the leap year challenge. first convert this function is_leap() so that instead of printing "leep year" or "not leep". 
It should return true or false. you are going to create new function called days_in_month() '''

def is_leap(year):
    if year % 4 == 0 :
        if year % 100 ==0 :
            if year % 400 ==0:
                return True
            else:
                return False
        else:
            return True
    else :
        return False

def days_in_month(year, month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month-1]

year= int(input("Enter the year: "))
month= int(input("Enter the month: "))
days= days_in_month(year, month)
print(days)