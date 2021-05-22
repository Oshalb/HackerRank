if __name__ == "__main__":
    for i in range(int(input().rstrip())):
        n, k = map(int, input().rstrip().split())
        a = list(map(int, input().rstrip().split()))
        a = sorted(a)
        la = len(a)
        c = 0
        for j in range(la):
            if a[j] <= 0:
                c += 1
            else:
                break
        print('YES' if c >= k else 'NO')
