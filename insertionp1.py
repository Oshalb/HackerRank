# Insertion Sort Part 1

def insertion_sort(n, arr):
    target = arr[-1]
    idx = n - 2

    while (target < arr[idx]) and (idx >= 0):
        arr[idx + 1] = arr[idx]
        print(*arr)
        idx -= 1

    arr[idx + 1] = target
    print(*arr)


if __name__ == "__main__":
    size_of_list = int(input())
    list_to_sort = list(map(int, input().rstrip().split()))
    insertion_sort(size_of_list, list_to_sort)
