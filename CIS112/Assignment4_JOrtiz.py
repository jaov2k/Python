# Jose Ortiz
# 03-10-2021
# CIS112 - Spring 2021
# Assignment 4

# PURPOSE:  To identify if a number is a prime number or not.
#           Taking user input, passing to a function, outputting
#           if the number is prime.
#           Then asking, "Y or N", if they want to "play again"

# FUNCTION NAME:
#     isPrime
# PURPOSE:
#     to determine whether an inputted number is a prime number
# PARAMETER:
#     int num
# RETURN VALUE:
#     bool
# FUNCTION SINGATURE:
#     isPrime(num)
 
def isPrime(num):
    prime = True    
    i = 2

    if num == 0 or num == 1:
        prime = False

    else:
        while i <= num / 2:
            if (num % i) == 0:
                prime = False
                break
            i += 1
    return prime

if __name__ == "__main__":
    while True:
        userNum = int(input('\n\n\nPlease enter a number: ').strip())
        print(f'{userNum} is a prime number') if isPrime(userNum) else print(f'{userNum} is not a prime number.')
        replay = input('Do you want to play again? (Y or N) ').lower()
        if replay == 'y':
            True
        else:
            print('\n\n\nThanks for playing.')
            break