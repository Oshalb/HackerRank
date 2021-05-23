if __name__ == "__main__":
    i, j, k = map(int, input().rstrip().split())
    count = 0
    for day in range(i, j+1):
        n = int(str(day)[::-1])
        if (abs(day - n)) % k == 0:
            count += 1
    print(count)
