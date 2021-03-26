# Jose Ortiz
# 03-26-2021
# CIS112 - Spring 2021
# Assignment 6
#
# PURPOSE:  A Python program which will take file name and it's content from the user.
#           Save all the input from the user to the file that was created.
#           Once user is done with providing the content, display the file content on the monitor.
#           Features include using Function passing, and RegEx.


#TODO: create file
#TODO: is fileName Proper. Filename, including extension must be A-Z,a-z, or '_'
#TODO: input sentence. Must prompt for addition sentences
#TODO: output file content
#TODO: #replay


import re

# PURPOSE:
# PARAMETERS:
# RETURN VALUES:
# FUNCTION SINGATURE:
def createFile():
    filename = input("Please enter a filename: ")
    print("Filename start is proper...") if re.findall("\A[a-z]|[A-Z]|_",filename) else print("improper filename")
    print("NUMBERS found...") if not re.findall("\d",filename) else print("No numbers allowed...")
    print("Special characters NOT found...") if not re.search("[+]",filename) else print ("No special characters allowed...")

if __name__ == "__main__":
    while True:
        createFile()
        replay = input("Play again? (y/n): ")
        if replay.lower() == 'y':
            continue
        else:
            break