# Write a recursive void function that has one parameter that is a positive integer.  When called, the function writes its argument to the screen backward.  That is,, if the argument is 1234, it outputs the following to the screen: 4321.

def rvrs_num(n):
    if n < 10:
        print(n, end="")
        return
    print(n % 10, end="")
    rvrs_num(n // 10)
arg = int(input("Enter your argument: "))
rvrs_num(arg)
print()
