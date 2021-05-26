import string

while True:
    while True:
        fileName = input('enter file name: ')
        try:
            fhand = open(fileName, 'r')
            break
        except:
            print('Error with file name') #if file name invalid, print error message
            continue
    
    data = fhand.read()
    words = data.split()
    d = {}
    specialChars = {ord('('):None,
                    ord(')'):None,
                    ord('-'):None,
                    ord(','):None,
                    ord(';'):None,
                    ord('.'):None}

    for word in words:        
        word = word.translate(specialChars)
        word = word.lower().strip()       
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    for key, value in sorted (d.items()):
        print(key, ':', value)

    print ('\nThere are', len(d),'different words in the file.\n')

    again = input('Do you want to try another file? (y or n) ')
    if again == 'y':
        continue
    else:
        print('Thank you for playing')
        break