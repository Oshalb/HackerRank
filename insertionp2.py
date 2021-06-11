# Insertion Sort - Part 2

def insertion_sort(n, a):
    for i in range(1, n):
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            j -=1
        print(*a)


if __name__ == "__main__":
    size_of_list = int(input())
    number_list = list(map(int, input().rstrip().split()))
    insertion_sort(size_of_list, number_list)
