# Recursion: Fibonacci Number

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    index_of_fibonacci_series = int(input())
    result = fib(index_of_fibonacci_series - 1)
    print(result)
