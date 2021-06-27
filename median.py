# Find the Median

def find_median(a):
    a.sort()
    m = len(a)/2
    return a[m]


if __name__ == "__main__":
    size_of_list = int(input())
    list_to_check = list(map(int, input().rstrip().split()))
    result = find_median(list_to_check)
    print(result)
