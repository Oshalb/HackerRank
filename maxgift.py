# Mark and Toy

def find_max_toys(t, k):
    t.sort()
    c, b = 0, 0
    for i in t:
        # Add price to b then compare with given budget
        b += i
        if b <= k:
            c += 1
        # Return number of toys if b in more than the budget
        else:
            return c


if __name__ == "__main__":
    number_of_toys, budget_for_toys = map(int, input().rstrip().split())
    list_of_toy_prices = list(map(int, input().rstrip().split()))
    result = find_max_toys(list_of_toy_prices, budget_for_toys)
    print(result)
