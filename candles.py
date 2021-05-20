if __name__ == '__main__':
    n = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    print(candles.count(max(candles)))
