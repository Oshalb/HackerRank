# Repeated String

def count_a(s, n):
    sl = len(s)
    c = s.count('a')
    d, m = divmod(n, sl)
    sc = s[0:m]
    c *= d
    c += sc.count('a')
    return c


if __name__ == "__main__":
    string = input()
    length = int(input())
    result = count_a(string, length)
    print(result)
