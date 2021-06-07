# Taum and B'day

def count_cost(b, w, bc, wc, z):
    if bc == wc:
        return (b * bc) + (w * wc)
    if wc > bc:
        if wc - bc <= z:
            return (b * bc) + (w * wc)
        else:
            c = bc + z
            return (b * bc) + (w * c)
    if wc < bc:
        if bc - wc <= z:
            return (b * bc) + (w * wc)
        else:
            c = wc + z
            return (b * c) + (w * wc)


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        black, white = map(int, input().split())
        black_cost, white_cost, change_cost = map(int, input().split())
        result = count_cost(black, white, black_cost, white_cost, change_cost)
        print(result)
