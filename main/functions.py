def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        print(a, end=' ')
        a, b = b, a+b
    return result

def insert_integer(): #ask for an integer and returns failure if not
    while True:
        try:
            result=int(input("Insert an integer (O for exit):"))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return result
    
    