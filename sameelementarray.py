# Equalize an Array
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    sa = set(arr)
    la = len(arr)
    c = [0] * 101
    for i in sa:
        for j in range(la):
            if i == arr[j]:
                c[arr[j]] += 1
    s = sum(c) - max(c)
    print(s)
