# Electronics Shop
def total_cost(b, k, d):
    c = 0
    for i in k:
        for j in d:
            z = i + j
            if c < z <= b:
                c = z
    return 0 if c == 0 else c


if __name__ == "__main__":
    budget, n, m = map(int, input().rstrip().split())
    keyboard = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    r = total_cost(budget, keyboard, drives)
    print(r)
