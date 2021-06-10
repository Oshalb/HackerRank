# Modified Kaprekar Number
import math


def check_range(p, q):
    r = []
    flag = 0
    for i in range(p, q+1):
        s = math.pow(i, 2)
        si = str(i)
        sil = len(si)
        g = math.pow(10, sil)
        su = s % g + s / g
        if su == i:
            r.append(i)
            flag = 1
    if flag == 0:
        print("INVALID RANGE")
    else:
        print(*r)


if __name__ == "__main__":
    start, end = int(input()), int(input())
    check_range(start, end)
