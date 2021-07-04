# Sherlock and Array

def find_num(a, n):
    s = sum(a)
    left = 0
    for i in range(n):
        current = a[i]
        s -= current
        if left == s:
            return 'YES'
        left += current
    return 'NO'


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        length_of_list = int(input())
        list_to_check = list(map(int, input().rstrip().split()))
        result = find_num(list_to_check, length_of_list)
        print(result)
