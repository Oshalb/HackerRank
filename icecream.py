# Ice Cream Parlor

def find_flavor(c, f):
    for i in range(len(f)):
        for j in range(i+1, len(f)):
            if f[i] + f[j] == c:
                return [i+1, j+1]
    return 0


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        total_money = int(input())
        number_of_flavor = int(input())
        cost_of_flavors = list(map(int, input().rstrip().split()))
        result = find_flavor(total_money, cost_of_flavors)
        print(*result, sep=' ')
