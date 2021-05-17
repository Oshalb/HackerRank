if __name__ == '__main__':
    n, k = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if i < j:
                if (arr[i] + arr[j]) % k == 0:
                    count += 1
    print(count)
