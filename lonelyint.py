# Lonely Integer

def find_integer(a):
    sa = set(a)
    r = []
    for i in sa:
        c = a.count(i)
        if c == 1:
            r.append(i)
    return r


if __name__ == "__main__":
    size_of_list = int(input())
    list_to_check = list(map(int, input().rstrip().split()))
    result = find_integer(list_to_check)
    print(*result, sep=' ')
