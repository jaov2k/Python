'''
Jose Ortiz
02-27-2021
CIS112 - Spring 2021
Assignment 1 
PURPOSE:
    This is a program which finds the number of days in a month by getting
    user input for year and month. It then determines how many days in the month
    and if it's a leap year add the additional day to February, 29 days.
'''
def IsLeap(year):
    return True if not(year % 4) else False

def GetDays():
    '''To determine number of days in a given month'''    
    year = int(input("Please enter the 4 digit year: "))
    month = int(input("Please enter the month: "))

    daysInMonths = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    if IsLeap(year) and month == 2:
        print(f"Year {year} Month 2 has 29 days in a month")
    else:
        print(f"Year {year} Month {month} has {daysInMonths[month]} days in a month")

if __name__=="__main__":
    while True:
        GetDays()
        if input("Do you want to repeat (Y/N): ").lower() == 'y':
            True
        else:
            print("\n\nThanks for playing!")
            break

