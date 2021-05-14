def countapplesandoranges(s, t, a, b, ap, o):
    ac = 0
    oc = 0
    for i in ap:
        su = a+i
        if su in range(s, t+1):
            ac += 1
    for j in o:
        os = b + j
        if os in range(s, t+1):
            oc += 1
    print(ac, oc, sep='\n')


if __name__ == "__main__":
    house = list(map(int, input().rstrip().split()))
    tree = list(map(int, input().rstrip().split()))
    #fruitnumber = list(map(int, input().rstrip().split))
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countapplesandoranges(house[0], house[1], tree[0], tree[1], apples, oranges)
