#Prof Huh CIS012 Assignment 7
#************************************** SAMPLE1.TXT **************************************#

#Variables
vowelList = 'AEIOUaeiou'
lines = 0
vowels = 0
consonants = 0
numbers = 0

#File IO
while True:
    filename = input("enter filename: ")
    try:
        myFile = open(filename,"r")
        break
    except:
        print("Incorrect filename or file does not exist. Try Again...")
data = myFile.read()
paragraphs = data.split("\n")

#Counting
for sentences in paragraphs:    
    for chars in sentences:
        if chars.isalpha():
            if chars in vowelList:
                vowels += 1
            else:
                consonants += 1
        elif chars.isdigit():
            numbers += 1
    lines += 1

#Printing
print (f"Total lines: {lines}\n"
       f"Total vowels: {vowels}\n"
       f"Total consonants: {consonants}\n"
       f"Total numbers: {numbers}\n")

#Closing
myFile.close()