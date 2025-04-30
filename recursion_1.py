# Write a recursive void function that has one parameter that is a positive integer and that writes out that number of asterisks (*) to the screen, all on one line.

def prntastrsks(n):
    if n == 0:
        return
    print("*", end="")
    prntastrsks(n - 1)
    
num = int(input("Type positive int: "))
prntastrsks(num)
print()
