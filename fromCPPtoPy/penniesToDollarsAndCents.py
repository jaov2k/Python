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

    print("In US currency you have: " + 
        str(int(dollars)) + " dollars " + 
        str(int(quarters)) + " quarters " + 
        str(int(dimes)) + " dimes " +
        str(int(nickles)) + " nickles " + 
        str(int(pennies)) + " pennies.\n" +
        "In Canadian currency you have: $" + str((int(numPennies * exchangeRate) / 100)) + " dollars.")


