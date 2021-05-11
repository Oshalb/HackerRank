if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            print(' ',end='')
        c = '#'*i
        print(c)
