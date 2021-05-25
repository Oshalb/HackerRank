if __name__ == "__main__":
    for i in range(int(input())):
        n = k = int(input())
        count = 0
        while k:
            r = k % 10
            k /= 10
            if r != 0 and n % r == 0:
                count += 1
        print(count)
