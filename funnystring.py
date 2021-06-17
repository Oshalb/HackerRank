# Funny String

def cal_diff(s):
    rs = s[::-1]
    ls = len(s)
    c = 0
    for i in range(ls-1):
        if (abs(ord(s[i]) - ord(s[i+1]))) != (abs(ord(rs[i]) - ord(rs[i+1]))):
            c += 1
    return 'Funny' if c == 0 else 'Not Funny'


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        string_to_check = str(input())
        result = cal_diff(string_to_check)
        print(result)
