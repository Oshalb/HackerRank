def kangaroo(x1, v1, x2, v2):
    return "YES" if v1 > v2 and (x2 - x1) % (v1 - v2) == 0 else "NO"


if __name__ == "__main__":
    n = list(map(int, input().rstrip().split()))
    x1, v1, x2, v2 = n[0], n[1], n[2], n[3]
    r = kangaroo(x1, v1, x2, v2)
    print(r)
