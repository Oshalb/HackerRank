# Sherlock and Squares
import math


def check_square(s, e):
    c = 0
    ss = math.floor(math.sqrt(s))
    if pow(ss, 2) == s:
        c += 1
    se = math.floor(math.sqrt(e))
    c += se - ss
    return c


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        start, end = map(int, input().split())
        result = check_square(start, end)
        print(result)
