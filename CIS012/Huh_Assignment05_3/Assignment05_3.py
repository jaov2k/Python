myList = [3,8,5,1,4,9,2,10,7]
evenTotal = 0
oddTotal = 0
smallest = myList[0]
largest = myList[0]

for i in myList:
    if i % 2:
        oddTotal += i
    else:
        evenTotal += i
    if smallest > i:
        smallest = i
    if largest < i:
        largest = i
        
print("Sum of even numbers: ", evenTotal)
print("Sum of odd numbers: ", oddTotal)
print("Largest number in the list is: ", largest)
print("Smallest number in the list is: ", smallest)