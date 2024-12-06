from functions import * 

fib.result = []

while True:
    fib.a=insert_integer()
    if fib.a == 0:
        break
    elif fib.a < 0:
        print("Negative numbers are not allowed")
    else:
        print("\n")
        fib.result=fib(fib.a)
        fib.result
        print("\n \n")

input("Press enter to exit")
