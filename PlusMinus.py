if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    nn, pn, z = 0, 0, 0
    l = len(arr)
    for i in arr:
        if i < 0:
            nn += 1
        elif i > 0:
            pn += 1
        elif i == 0:
            z += 1
    pr = float(pn / l)
    nr = float(nn / l)
    zr = float(z / l)
    print(pr)
    print(nr)
    print(zr)