if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input().strip())
        c = 1
        if n == 0:
            print(1)
        else:
            c = 2
            for j in range(1, n + 1):
                if j % 2 == 0:
                    c *= 2
                else:
                    c += 1
            print(c)
