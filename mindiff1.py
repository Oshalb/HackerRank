# Minimum Absolute Difference in an Array

def check_diff(a):
    diff = int('inf')
    a.sort()
    for i in range(len(a) - 1):
        m = abs(a[i] - a[i + 1])
        if diff > m:
            diff = m
    return diff


if __name__ == "__main__":
    size_of_list = int(input())
    list_to_check = list(map(int, input().rstrip().split()))
    result = check_diff(list_to_check)
    print(result)
