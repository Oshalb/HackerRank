if __name__ == "__main__":
    n, k = map(int, input().rstrip().split())
    c = list(map(int, input().rstrip().split()))
    e = 100
    i = k % n
    e -= c[i] * 2 + 1
    while i != 0:
        i = (i + k) % n
        e -= c[i] * 2 + 1
    print(e)
