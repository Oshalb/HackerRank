# Cut the Sticks
if __name__ == "__main__":
    n = input()
    lis = list(map(int, input().rstrip().split()))
    while True:
        lis = [i for i in lis if i != 0]
        l = len(lis)
        if l > 0:
            m = min(lis)
        else:
            break
        lis = [x - m for x in lis]
        print(len(lis))
