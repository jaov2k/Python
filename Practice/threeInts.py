#Write a Python program that prompts the user to input three integers.
#The Python program should convert the user input to integers. You should use try except to protect the program from crashing if the user puts in bad input.
#The program should then output the numbers in ascending order (like 1, 2, 3) using a chained conditional.
#The program should also output the numbers in descending order (like 3, 2, 1) using nested conditionals.
#Test your program.

#First, asking user for input
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
  
except:
    print("Please enter a number")

#SMALLEST NUMBER
if a < b and a < c:
    small = a
elif b < c and b < a:
    small = b
else:
    small = c
   
#MIDDLE NUMBER
if (a < c and a > b) or (a < b and a > c):
    middle = a
elif (b > a and b < c) or (b > c and b < a):
    middle = b
elif (c > a and c < b) or (c > b and c < a):
    middle = c

#LARGEST NUMBER
if a > b and a > c:
    large = a
elif a < b and c < b:
    large = b
else:
    large = c

#Now displaying user input which is sorted high to low, low to high
print("The numbers in ascending order are: ", small, middle, large)
print("The numbers in descending order are: ", large, middle, small)