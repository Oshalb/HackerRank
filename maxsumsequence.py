# The Maximum Subarray
import bisect


def max_sum_array(numbers):
    best_sum = float('-inf')
    best_start = best_end = 0  # or: None
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = x
        else:
            # Extend the existing sequence with the current element
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1  # the +1 is to make 'best_end' exclusive

    return best_sum, best_start, best_end


def main():
    size_of_list = int(input())
    list_to_check = list(map(int, input().rstrip().split()))
    a = [x for x in list_to_check]
    if len(a) == 0:
        print(0, 0)
        return True
    a.sort()
    i = bisect.bisect(a, 0)
    b = a[:i]
    c = a[i:]
    if len(b) == 0:
        p = sum(c)
        print(p, p)
        return True
    elif len(c) == 0:
        p = max(b)
        print(p, p)
        return True
    else:
        result, s, e = max_sum_array(list_to_check)
        print(result, end=' ')
        result = max(sum(c), max(b))
        print(result)


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        main()
