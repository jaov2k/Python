#PURPOSE:   To convert a stack of pennies into 
#           typical denominations.

def breakCash(numPennies):
    dollars = int(numPennies / 100)
    quarters = int((numPennies % 100) / 25)
    dimes = int(((numPennies % 100) % 25) / 10)
    nickles = int((((numPennies % 100) % 25) % 10) / 5)
    pennies = int((((numPennies % 100) % 25) % 10) % 5)
    exchangeRate = 1.33

    return  (f'In US currency you have:{dollars} dollars, {quarters} quarters, {dimes} dimes, {nickles} nickles, and {pennies} pennies.\n'
            f'In Canadian currency you have: ${(numPennies * exchangeRate / 100):0.2f}')

if __name__ == "__main__":
    print(breakCash(int(input("Please enter all of your pennies: "))))
