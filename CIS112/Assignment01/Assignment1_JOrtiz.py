'''
Jose Ortiz
02-27-2021
CIS112 - Spring 2021
Assignment 1 
PURPOSE:
    This is a program which finds the number of days in a month by getting
    user input for year and month. It then determines how many days in the month
    and if it's a leap year add the additional day to February, 29 days.'''

# START code here
def IsLeap(year):
    ''' Tests whether the inputted year is a leap year
        and if so return True so it can be used by the 'if'
        statement from the GetDays() function.'''

    return True if not(year % 4) else False

def GetDays():
    ''' Determines number of days in a given month
        and whether its a leap year'''    

    year = int(input("Please enter the 4 digit year: "))
    month = int(input("Please enter the month: "))

    daysInMonths = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

#   First test if its a 29 day February, otherwise its typical.
    if IsLeap(year) and month == 2:
        print(f"Year {year} Month 2 has 29 days in a month")
    else:
        print(f"Year {year} Month {month} has {daysInMonths[month]} days in a month")

# Main loop
if __name__=="__main__":
    while True:
        GetDays()
        if input("Do you want to repeat? (Y/N): ").lower().strip() == 'y':
            True
        else:
            print("\n\nThank you for playing!")
            break
#END code here