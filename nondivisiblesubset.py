# Non-Divisible Subset
import math


def check_if_divisible(s, k):
    s = sorted(s)
    sl = len(s)
    c = 0
    m = [0]*k
    for i in s:
        m[i % k] += 1
    if m[0] > 0:
        c = 1
    for i in range(1, int(k/2)+1):
        if i == k-i:
            c += 1
        else:
            c += max(m[i], m[abs(k-i)])
    # print(s, m, sep='\n')
    return c


if __name__ == "__main__":
    length_of_set, number = map(int, input().split())
    arr = list(map(int, input().rstrip().split()))
    result = check_if_divisible(arr, number)
    print(result)
