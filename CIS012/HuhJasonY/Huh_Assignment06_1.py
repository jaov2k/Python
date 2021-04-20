#Jose Ortiz
#04-19-2021
#CIS012 - Assignment 06_1
#PURPOSE:   
#   Your program will take a string as an input and using slice and find function, to extract a string after a colon.
#   Then, convert it to floating point number and add 2.0 to it.

s = input('Enter a string with a colon and a number after it: ')
print('Extracted a number from given string and added 2.0 to it:', float(s[s.find(':') + 2:]) + 2)