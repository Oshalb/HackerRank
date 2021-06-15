# Quicksort - 2 Sorting

def quicksort(a, lo, hi):
    if lo < hi:
        p = partition(a, lo, hi)
        quicksort(a, lo, p - 1)
        quicksort(a, p + 1, hi)


def partition(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i = i + 1
    a[i], a[hi] = a[hi], a[i]
    return i


if __name__ == "__main__":
    length_of_list = int(input())
    list_to_sort = list(map(int, input().rstrip().split()))
    quicksort(list_to_sort, 0, length_of_list-1)
    print(list_to_sort)
