a = "This is !A Test! see?"
firstBang = a.find("!")
secondStr = a[firstBang + 1:]
secondBang = secondStr.find("!")
finalStr = secondStr[ : secondBang]


i = len(finalStr) - 1
while i >= 0:
    print(finalStr[i])
    i -= 1