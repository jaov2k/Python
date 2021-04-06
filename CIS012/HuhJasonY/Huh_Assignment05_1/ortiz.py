def CalPay(hrs, rate):
    print("Hours entered are: ", hrs)
    print("Rate enteres is: ", rate)
    

def getInput(str):
    while True:
        if str == "hours":
            inp = input("Please enter hours: ") #strings
        elif str == "rate":
            inp = input("Please enter rate: ") #strings
        try:
            inp = float(inp)
        except ValueError:
            print ("No string permitted")
            continue
        if inp < 0:
            print ("No negative numbers")
        else:
            return inp

if __name__ == "__main__":
  while True:
    CalPay(getInput("hours"), getInput("rate"))    
    replay = input("Would you like to calc again (y/n): ")    
    if replay.lower() == 'y':
        continue
    else:
        print("Exiting...")
        break