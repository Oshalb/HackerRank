# Service Lane
if __name__ == "__main__":
    n, t = map(int, input().rstrip().split())
    width = list(map(int, input().rstrip().split()))
    for i in range(t):
        a, b = map(int, input().rstrip().split())
        m = 99999
        for j in width[a:b+1:1]:
            if j < m:
                m = j
        print(m)
