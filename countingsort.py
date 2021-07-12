# Counting Sort 2

def sort_list(a):
    sa = set(a)
    r = [0] * 100
    z = []
    for i in sa:
        r[i] = a.count(i)
    for i, b in enumerate(r):
        if b != 0:
            for j in range(b):
                z.append(i)
    return z


if __name__ == "__main__":
    length_of_list = int(input())
    list_to_sort = list(map(int, input().rstrip().split()))
    result = sort_list(list_to_sort)
    print(*result, sep=' ')
