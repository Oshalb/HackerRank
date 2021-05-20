if __name__ == "__main__":
    n, k = map(int, input().split())
    h = list(map(int, input().rstrip().split()))
    h = sorted(h, reverse=True)
    diff = h[0] - k
    print(0 if diff <= 0 else diff)
