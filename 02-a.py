def fibonacci(n):
    if n < 0:
        print("Invalid Input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


a = int(input("Enter a number: "))
print(fibonacci(a))