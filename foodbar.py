# Jim and the Orders

def give_order(d):
    ld = len(d)
    for i in range(1, ld + 1):
        d[i] = sum(d[i])
    nd = {}
    for key, value in d.items():
        if value in nd:
            nd[value].append(key)
        else:
            nd[value] = [key]
    snd = sorted(nd)
    r = []
    for i in snd:
        for j in nd[i]:
            r.append(j)
    return r


if __name__ == "__main__":
    number_of_customers = int(input())
    dictionary_of_customers = {}
    for k in range(1, number_of_customers+1):
        dictionary_of_customers[k] = list(map(int, input().rstrip().split()))
    result = give_order(dictionary_of_customers)
    print(*result, sep=' ')
