# Beautiful Triplets

def count_triplets(a, d, n):
    c = 0
    for i in range(n):
        if a[i] + d in a and a[i] + 2*d in a:
            c += 1
    return c


if __name__ == "__main__":
    size, difference = map(int, input().split())
    arr = list(map(int, input().rstrip().split()))
    result = count_triplets(arr, difference, size)
    print(result)
