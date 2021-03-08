# Create the following lists:

# inStock - 2D list (row size:10, column size:4)
# alpha - 1D list with 20 elements.
# beta - 1D list with 20 elements.
# gamma = [11, 13, 15, 17]
# delta = [3, 5, 2, 6, 10, 9, 7, 11, 1, 8]

 

# a. Write the definition of the function setZero that initializes any one-dimensional list to 0 (alpha and beta).

# b. Write the definition of the function inputArray that prompts the user to input 20 numbers and stores the numbers into alpha.

# c. Write the definition of the function doubleArray that initializes the elements of beta to two times the corresponding elements in alpha.  

# d. Write the definition of the function copyGamma that sets the elements of the first row of inStock from gamma and the remaining rows of inStock to three times the previous row of inStock.  

# e. Write the definition of the function copyAlphaBeta that stores alpha into the first five rows of inStock and beta into the last five rows of inStock.  

# f. Write the definition of the function printArray that prints any one-dimensional list.  The function must contain only one loop to print any one-dimensional list.  

# g. Write the definition of the function setInStock that prompts the user to input the elements for the first column of inStock.  
#    The function should then set the elements in the remaining columns to two times the corresponding element in the previous column, minus the corresponding element in delta.

inStock = [[0 for i in range(4)] for i in range(10)]
alpha = []
beta = []
gamma = [11, 13, 15, 17]
delta = [3, 5, 2, 6, 10, 9, 7, 11, 1, 8]

def setZero(array):
    array = [0 for i in range(20)]
    return array

def inputArray(array):
    print("\nEnter 20 integers:\n")
    printArray(array)

def doubleArray(arrayA, arrayB):
    pass

def copyGamma(arrayA, arrayB, arrayC):
    pass

def copyAlphaBeta():
    pass

def printArray(array):
    for i in range(len(array)):
        print(array[i], "\t", end='')
        if i == 9:
            print()

def setInStock():
    pass

if __name__ == "__main__":
    print("Alpha after initialization:")
    printArray(setZero(alpha))
    inputArray(alpha)