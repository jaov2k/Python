def setZero(array:list)->list:
    '''The setZero function initializes a single dimension array to 20 elements of 0'''
    array = [0 for i in range(20)]
    return array

def inputArray(array: list) -> list:
    '''The inputArray function asks the user for 20 integers.'''
    print('\n\nEnter 20 integers:')
    for i in range(len(array)):
        # safe to uncomment when finished testing
        #array[i] = int(input())

        #for testing purposes        
        array[i] = i + 1
        print(array[i])
    return array

def doubleArray(arrayA:list, arrayB:list) -> list:
    '''The doubleArray function doubles the first array's element values, 
       and places them in the second array'''
    for i in range(len(arrayA)):
        arrayB[i] = arrayA[i] * 2
    return arrayB

def copyGamma(arrayA:list, arrayB:list) -> list:
    '''The function copyGamma sets the elements of the first row of arrayA from arrayB,
       and the remaining rows of inStock to three times the previous row of arrayA.'''
    for i in range(len(arrayB)):
        arrayA[i] = arrayB[i]
    return arrayA

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
    inStock = [[0 for i in range(4)] for i in range(10)]
    alpha = []
    beta = []
    gamma = [11, 13, 15, 17]
    delta = [3, 5, 2, 6, 10, 9, 7, 11, 1, 8]

    alpha = setZero(alpha)
    beta = setZero(beta)

    print("\nAlpha after initialization:")
    printArray(alpha)
    alpha = inputArray(alpha)
    print('\n\nAlpha after reading 20 numbers:')
    printArray(alpha)    
    beta = doubleArray(alpha, beta)
    print('\n\nBeta after a call to doubleArray:')
    printArray(beta)
    inStock = copyGamma(inStock, gamma)
    print('\n\ninStock after a call to copyGamma:')
    printArray(inStock)