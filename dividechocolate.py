if __name__ == "__main__":
    n = int(input())
    s = list(map(int, input().rstrip().split()))
    d, m = map(int, input().split())
    count = 0
    for i in range(n):
        su = 0
        for j in range(i, i + m):
            if j < n:
                su += s[j]
        if su == d:
            count += 1
    print(count)
