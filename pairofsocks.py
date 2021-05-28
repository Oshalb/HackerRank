# Sales by Match
def pair_count(a):
    sa = set(a)
    count = 0
    for i in sa:
        e = a.count(i)
        if e % 2 == 0:
            count += int(e / 2)
        else:
            e -= 1
            if e > 1:
                count += int(e / 2)
    return count


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    r = pair_count(arr)
    print(r)
