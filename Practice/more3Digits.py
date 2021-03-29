def myFunc(a, b, c):
    if a <= b <= c:
        print("The numbers in ascending order are: ", a, b, c)
        print("The numbers in descending order are: ", c, b, a)
    elif a <= c <= b:
        print("The numbers in ascending order are: ", a, c, b)
        print("The numbers in descending order are: ", b, c, a)
    elif b <= a <= c:
        print("The numbers in ascending order are: ", b, a, c)
        print("The numbers in descending order are: ", c, a, b)
    elif c <= a <= b:
        print("The numbers in ascending order are: ", a, b, c)
        print("The numbers in descending order are: ", c, b, a)
    elif b <= c <= a:
        print("The numbers in ascending order are: ", c, a, b)
        print("The numbers in descending order are: ", b, a, c)
    elif c <= b <= a:
        print("The numbers in ascending order are: ", c, b, a)
        print("The numbers in descending order are: ", a, b, c)
        print ("Numbers ascending: ", a, b, c)

if __name__=="__main__":
    x, y, z = [int(i) for i in input("Enter 3 numbers (ex.:1 2 3): ").split()]
    myFunc(x, y, z)