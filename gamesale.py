# Halloween Sale

def count_game(p, d, m, b):
    g = ((p - m) / d) + 1
    ap = d * (((g-1)*g)/2)
    c = p * g - ap
    s = p - (m * d)
    while True:
        if c < b:
            t = b - c
            g += int(t / m)
            return g
        elif c > b:
            g -= 1
            c -= s
            s += 3
        else:
            return g


if __name__ == "__main__":
    price, discount, minimum_cost, budget = map(int, input().split())
    result = count_game(price, discount, minimum_cost, budget)
    print(result)
