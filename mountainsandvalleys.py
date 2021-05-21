if __name__ == "__main__":
    steps = int(input().strip())
    path = input().rstrip()
    seaLevel, valley = 0, 0

    for step in path:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1

        if step == 'U' and seaLevel == 0:
            valley += 1
    print(valley)
