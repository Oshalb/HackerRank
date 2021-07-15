# Sorting: Bubble Sort

def sort_list(a):
    c = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                c += 1
    return c


if __name__ == "__main__":
    size_of_list = int(input())
    list_to_sort = list(map(int, input().rstrip().split()))
    result = sort_list(list_to_sort)
    print("Array is sorted in", result, "swaps.")
    print("First Element:", list_to_sort[0])
    print("Last Element:", list_to_sort[-1])
