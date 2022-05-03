def fibonacci(n):
    a = 0
    b = 1

    if n < 0:
        print("value need to be greater than 0")

    elif n == 0:
        return a
    
    elif n == 1:
        return b
    else:
        for i in range (1,n):
            c = a+b
            a = b
            b = c
        return b


print(fibonacci(7))