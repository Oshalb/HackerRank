# Chocolate Feast

def feast(n, c, m):
    t = n / c
    w = t
    while w > m:
        t += int(w / m)
        w = int((w / m)) + int((w % m))
    return int(t)


if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        total_money, chocolate_price, wrapper = map(int, input().split())
        result = feast(total_money, chocolate_price, wrapper)
        print(result)
