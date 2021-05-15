import math

if __name__ == "__main__":
    n, m = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    la = a[0]
    for i in range(1, n):
        la = math.lcm(la, a[i])
    gb = b[0]
    for i in range(1, m):
        gb = math.gcd(gb, b[i])
    nu = []
    num = []
    for i in range(la, gb+1):
        nu.append(i)
    for i in nu:
        c = 0
        for j in a:
            if i % j == 0:
                c += 1
                if c == n:
                    num.append(i)
    nu = num
    num = []
    for i in nu:
        c = 0
        for j in b:
            if j % i == 0:
                c += 1
                if c == m:
                    num.append(i)
    count = len(num)
    print(count)
