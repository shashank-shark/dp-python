def fibonacci(n):

    fibPrev = 0
    fibNext = 1

    if (n == 0):
        return fibPrev
    if (n == 1):
        return fibNext

    return fibonacci(n-1) + fibonacci(n-2)

def main():
    return fibonacci(10)

print(main())