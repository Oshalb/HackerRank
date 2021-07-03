# Anagram

def check_anagram(s):
    ls = len(s)
    if ls % 2 != 0:
        return -1
    else:
        hls = int(ls/2)
        s1 = s[0:hls+1]
        s2 = s[hls:ls]
        a = set(s1).intersection(s2)
        b, c = 0, 0
        for i in a:
            b += min(s1.count(i), s2.count(i))
        r = abs(b - (len(s1)))
        return r


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        string_to_check = str(input())
        result = check_anagram(string_to_check)
        print(result)
