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

def isProperFirstChar(fname:str) -> bool:
    '''To check whether the first character of the filename meets the criteria'''
    fnameRE = re.compile(r'\A[^a-zA-z_]')
    if fnameRE.findall(fname):
        print('Filename only can start with Alphabets or "_".')
        return False
    else:
        print("Valid first character...")
        return True

def isProperExtension(fname:str) -> bool:
    '''To check whether the filename contains a '.' thus an extension'''
    fnameRE = re.compile(r'[\.]')
    if fnameRE.findall(fname):
        print("Valid extension...")
        return True
    else:
        print("File name needs to have an extension.")
        return False

def isProperFilename(fname:str) -> bool:
    '''To check whether the filename meets the criteria'''
    fnameRE = re.compile(r'[^a-zA-Z0-9\_\.]')
    if fnameRE.findall(fname):
        print('Filename can contain only Alphabets, digits and "_".')
        return False
    else:
        print("Valid filename...")
        return True

def createFile():
    #fname = input('Enter a fname: ')
    fname = "Th1s_1s_4_Pr0p3r_N4m3.7x7"
    print ("The fname entered was: ", fname)

    if isProperExtension(fname) and isProperFirstChar(fname) and isProperFilename(fname):
        print ("filename good...")
    else:
        print("filename bad...")

if __name__ == "__main__":
    createFile()
    # while True:
    #     createFile()
    #     replay = input("Play again? (y/n): ")
    #     if replay.lower() == 'y':
    #         continue
    #     else:
    #         break