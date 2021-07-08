# Sherlock and The Beast

def create_number(n):
    d = n
    while n % 3 != 0:
        n -= 5
    if n < 0:
        return -1
    else:
        return '5' * n + '3' * (d - n)


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        length_of_number = int(input())
        result = create_number(length_of_number)
        print(result)
