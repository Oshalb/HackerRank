# Alternating Characters

def check_string(s):
    a = set(s)
    ls = len(s)
    c = 1
    if len(a) == 1:
        return ls - 1
    else:
        i = 0
        while i < ls-1:
            if s[i] != s[i+1]:
                c += 1
            i += 1
    return ls - c


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        string_to_check = str(input())
        result = check_string(string_to_check)
        print(result)
