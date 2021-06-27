# Absolute Permutation

def find_permutation(n, d):
    k = {i : 0 for i in range(1, n+1)}
    r = []
    print(k)
    for i in range(1, n+1):
        if (k[i] == 0) and (i+d <= n):
            # print(i)
            k[i] = i + d
            k[i+d] = i
    # k[1] = 30
    print(k)
    for i in range(1, n+1):
        if k[i] == 0:
            return -1
        else:
            r.append(k[i])
    return r


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        range_to_check, difference_between_permutation = map(int, input().rstrip().split())
        result = find_permutation(range_to_check, difference_between_permutation)
        if result == -1:
            print(-1)
        else:
            print(*result, sep=' ')
