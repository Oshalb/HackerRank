# New Year Chaos

def count_bribe(a):
    c = 0
    for i, j in enumerate(a, 1):
        if j - i > 2:
            return "Too chaotic"
        else:
            for k in range(max(j - 2, 0), i):
                if a[k] > j:
                    c += 1
    return c


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        length_of_list = int(input())
        list_to_check = list(map(int, input().rstrip().split()))
        result = count_bribe(list_to_check)
        print(result)
