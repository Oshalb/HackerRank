# Viral Advertising
import math

if __name__ == "__main__":
    n = 5
    c = 0
    for i in range(int(input())):
        n = math.floor(n / 2)
        c += n
        n *= 3
    print(c)
