import math

if __name__ == '__main__':
    for i in range(int(input())):
        k = int(input().strip())
        f = math.ceil(k / 2)
        s = k - f
        print(f * s)
