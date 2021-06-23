# Pairs

import sys


def check_pairs(a, k):
    a.sort()
    left = 0
    right = 1
    answer = 0
    while right < len(a):
        val = a[right]-a[left]
        if val == k:
            answer += 1
            left += 1
            right += 1
        elif val < k:
            right += 1
        else:
            left += 1
            if left == right:
                right += 1

    return answer


if __name__ == "__main__":
    length_of_list, difference_to_check = map(int, sys.stdin.readline().strip().split())
    list_to_check = list(map(int, sys.stdin.readline().rstrip().split()))
    result = check_pairs(list_to_check, difference_to_check)
    sys.stdout.write(str(result))
