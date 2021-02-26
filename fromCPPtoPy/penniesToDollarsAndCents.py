if __name__ == "__main__":

#   PURPOSE:  this console program breaks the total number of pennies into 
#           respective USD and CAN denominations, and print the string buffer 
#           containing the entire formatted output string to the console display
#   PARAMETERS:
#      	    None
#   RETURN VALUES:
#      	    None
    numPennies = int(input("Please enter all of your pennies: "))
    dollars = numPennies / 100
    quarters = (numPennies % 100) / 25
    dimes = ((numPennies % 100) % 25) / 10
    nickles = (((numPennies % 100) % 25) % 10) / 5
    pennies = (((numPennies % 100) % 25) % 10) % 5
    exchangeRate = 1.33

    #New formatting using fString
    print(f"In US currency you have: {dollars:.0f} dollars, {quarters:.0f} quarters, {dimes:.0f} dimes, {nickles:.0f} nickles, {pennies:.0f} pennies.\n" +
          f"In Canadian currency you have: ${(numPennies * exchangeRate / 100):.2f} dollars.")

    #Old School formatting
    print("In US currency you have: %d dollars, %d quarters, %d dimes, %d nickles, %d pennies.\n"%(dollars, quarters, dimes, nickles, pennies) +
          "In Canadian currency you have: $%.2f dollars."%(numPennies * exchangeRate / 100))


