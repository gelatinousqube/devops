def fibonacci(n):
   
    if n < 0:
        print("value need to be greater than 0")
 
   
    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Driver Program
print(fibonacci(9))