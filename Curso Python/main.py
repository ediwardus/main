from functions import * 

fib.result = []

print("...:::Fibonacci Series Generator:::...")

while True:
    fib.a=float(input("Insert a positive integer (O for exit):"))
    if fib.a == 0:
        break
    elif fib.a < 0:
        print("Negative numbers are not allowed")
    elif fib.a%1!=0:
        print("Floats not allowed")
    else:
        fib.result=fib(fib.a)
        fib.result
        print()

input("Press enter to exit")