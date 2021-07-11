# Counting Sort 1

def count_frequency(a):
    c = [0] * 100
    sa = set(a)
    for i in sa:
        c[i] = a.count(i)
    return c


if __name__ == "__main__":
    length_of_list = int(input())
    list_to_check = list(map(int, input().rstrip().split()))
    result = count_frequency(list_to_check)
    print(*result, sep=' ')
