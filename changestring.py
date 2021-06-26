# The Love-Letter Mystery

def string_to_palindrome(s):
    ls = len(s)
    c = 0
    for i in range(int(ls/2)):
        if s[i] != s[-(i+1)]:
            c += abs(ord(s[i]) - ord(s[-(i+1)]))
    return c


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        string_to_change = str(input())
        result = string_to_palindrome(string_to_change)
        print(result)
