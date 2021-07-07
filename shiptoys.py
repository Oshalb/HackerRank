# Priyanka and Toys

def count_weight(w):
    w.sort()
    r = 1
    f = w[0]
    for i in w:
        c = list(range(f, f+5))
        if i not in c:
            f = i
            r += 1
    return r


if __name__ == "__main__":
    number_of_toys = int(input())
    list_of_weights = list(map(int, input().rstrip().split()))
    result = count_weight(list_of_weights)
    print(result)
