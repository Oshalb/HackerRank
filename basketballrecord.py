if __name__ == '__main__':
    n = int(input().strip())
    score = list(map(int, input().rstrip().split()))
    record = [0, 0]
    mi = score[0]
    ma = score[0]
    for i in score:
        if i > ma:
            ma = i
            record[0] += 1
        elif i < mi:
            mi = i
            record[1] += 1
    print(*record, sep=" ")
