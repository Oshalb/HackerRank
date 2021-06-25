# Closest Numbers

def find_pairs(a):
    sa = sorted(set(a))
    m = 9999999999
    r = []
    for i in range(len(sa)-1):
        diff = sa[i] - sa[i+1]
        if diff < m:
            m = diff
    for i in range(len(sa)-1):
        diff = sa[i] - sa[i + 1]
        if diff == m:
            r.append(sa[i])
            r.append(sa[i+1])
    return r


if __name__ == "__main__":
    length_of_list = int(input())
    list_to_check = list(map(int, input().rstrip().split()))
    result = find_pairs(list_to_check)
    print(*result, sep=" ")
