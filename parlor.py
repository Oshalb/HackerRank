# Hash Tables: Ice Cream Parlor

def find_prices(m, p):
    d = {}
    for i, n in enumerate(p, 1):
        if m - n in d:
            return [d[m-n], i]
        d[n] = i


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        total_amount = int(input())
        length_of_list = int(input())
        list_of_prices = list(map(int, input().rstrip().split()))
        result = find_prices(total_amount, list_of_prices)
        print(*result, sep=' ')
