# Grid Challenge

def sort_and_check(s):
    ls = len(s)
    for i in range(ls):
        s[i] = sorted(s[i])
    lsc = len(s[0])
    for i in range(ls-1):
        for j in range(lsc):
            if s[i][j] > s[i+1][j]:
                return "NO"
    return "YES"


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        grid_size = int(input())
        grid_to_check = []
        for z in range(grid_size):
            grid_to_check.append(str(input()))
        result = sort_and_check(grid_to_check)
        print(result)
