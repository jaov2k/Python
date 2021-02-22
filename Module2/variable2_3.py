#Operators
if __name__ == "__main__":
    left = 10
    right = 3
    leftStr = 'Ten'
    result = left + right
    print("Addition")
    print(left ," + ", right, " = ", left + right)
    print("Subtraction")
    print(left ," - ", right, " = ", left - right)
    print("Multiplication")
    print(left ," * ", right, " = ", left * right)
    print("Division")
    print(left ," / ", right, " = ", left / right)
    print("Integer Division")
    print (left ," // ", right, " = ", left // right)
    print("Modulo")
    print (left ," % ", right, " = ", left % right)
    print("Exponentiation")
    print (left ," ** ", right, " = ", left ** right)
    print("Using '+' for concatination")
    print(leftStr ," + ", leftStr ," + ", leftStr, " = ", leftStr + leftStr + leftStr)
    print("Using '*' for concatination")
    print(leftStr ," * ", right, " = ", leftStr * right)

    left = [1,2,3]
    right = [4,5,6]
    print("\nConcatinate two lists")
    print(left)
    print(right)
    print(left + right)
