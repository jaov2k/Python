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
    #fname = input('Enter a fname: ')
    fname = "!?1s_1s_4_Pr0p3r_N4m3.7x7"
    print ("The fname entered was: ", fname)
    
    #Check first character
    fnameRE = re.compile(r'\A[^a-zA-z_]')
    if fnameRE.findall(fname):
        print("Invalid first character. Only A-Z, a-z, or '_'")
        print ('"', *fnameRE.findall(fname), '"', end=' - is invalid\n')
    else:
        print("Valid first character...")

    #Check fname
    fnameRE = re.compile(r'(\W)\.(\W){3}')
    if fnameRE.search(fname):
        print("Invalid fname. Only A-Z, a-z, 0-9, or '_'")
        print ('"', *fnameRE.findall(fname), '"', end=' - is invalid\n')
    else:
        print("Valid fname...")



if __name__ == "__main__":
    createFile()
    # while True:
    #     createFile()
    #     replay = input("Play again? (y/n): ")
    #     if replay.lower() == 'y':
    #         continue
    #     else:
    #         break