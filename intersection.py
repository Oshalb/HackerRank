# Missing Numbers

def list_intersection(l1, l2):
    f, s = set(l1), set(l2)
    u = f.union(s)
    t = f.intersection(s)
    r = []
    for i in u:
        if i not in t:
            r.append(i)
    for i in t:
        if l1.count(i) != l2.count(i):
            if i in r:
                pass
            else:
                r.append(i)
    return sorted(r)


if __name__ == "__main__":
    size_of_first_list = int(input())
    first_list = list(map(int, input().rstrip().split()))
    size_of_second_list = int(input())
    second_list = list(map(int, input().rstrip().split()))
    result = list_intersection(first_list, second_list)
    print(*result, sep=' ')
