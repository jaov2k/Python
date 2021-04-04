#this is prof. Huh HW5_2
while True:
    evenTotal = 0
    oddTotal = 0
    print("Enter 6 numbers:\n")
    i = 0
    while i < 6:
        num = int(input(">"))
        if(num % 2):
            oddTotal += num
        else:
            evenTotal += num
        i += 1
    print("Even numbers: ", evenTotal)
    print("Odd numbers: ", oddTotal)
    repeat = input("Do you want to play again (y/n): ")
    if(repeat == 'y'):
        continue
    else:
        print("Thanks for playing!...")
        break