# PURPOSE:  Small program to display the Nim game
#           Its a single pile of pebbles.
#           Players can take 1 to 8 stones per turn.

def canAlwaysWin(n):
    if 0 < n:
        return True if n % 9 else False

if __name__ == "__main__":
    print(canAlwaysWin(int(input("Enter a number: "))))