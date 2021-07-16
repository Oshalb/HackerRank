# Permuting Two Array

def permute_list(a, b, n, k):
    a = sorted(a)
    b = sorted(b, reverse=True)
    for i in range(n):
        if a[i] + b[i] < k:
            return "NO"
    return "YES"


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        size_of_list, difference_to_check = map(int, input().rstrip().split())
        first_list = list(map(int, input().rstrip().split()))
        second_list = list(map(int, input().rstrip().split()))
        result = permute_list(first_list, second_list, size_of_list, difference_to_check)
        print(result)
