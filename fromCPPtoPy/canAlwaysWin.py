def canAlwaysWin(n):
    if 0 < n:
        return True if n % 9 else False

if __name__ == "__main__":
    print(canAlwaysWin(int(input("Enter a number: "))))