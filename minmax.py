if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    arr = sorted(arr)
    mi = arr[0] + arr[1] + arr[2] + arr[3]
    ma = arr[1] + arr[2] + arr[3] + arr[4]
    print(mi, ma)
