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
        return True

def isProperExtension(fname:str) -> bool:
    '''To check whether the filename contains a '.' thus an extension'''
    fnameRE = re.compile(r'[\.]')
    if fnameRE.findall(fname):
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
        return True

def createFile():
    fname = input('Please enter a filename: ')
    if isProperFirstChar(fname) and isProperExtension(fname) and isProperFilename(fname):
        while True:
            with open(fname, "a+" ) as file:
                content = input("Please enter a sentence: ") + "\n"
                file.write(content)             
            if input("Do you want to add more lines? (Y/N) ").lower() == 'y':
                continue
            else:
                break

        with open(fname,"r") as file:
            print("This is what's entered into file", fname)
            print("=============================")
            content = file.readlines()
            for line in content:                
                print(line, end='\r')
            print("=============================")
    else:
        print("filename bad...")

if __name__ == "__main__":
    while True:
        createFile()
        replay = input("Do you want to create another file? (Y/N) ")
        if replay.lower() == 'y':
            print("Let's create another file.")
            continue
        else:
            print("Thank you for playing!")
            break