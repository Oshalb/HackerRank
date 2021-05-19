if __name__ == '__main__':
    n, k = map(int, input().rstrip().split())
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    rba = int((sum(bill)-bill[k])/2)
    if b == rba:
        print("Bon Appetit")
    else:
        print(b - rba)
