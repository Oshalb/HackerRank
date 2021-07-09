# Games of Thrones - 1

def check_palindrome(s):
    set_s = set(s)
    length_s = len(s)
    if length_s % 2 == 0:
        for i in set_s:
            if s.count(i) % 2 != 0:
                return "NO"
            elif s.count(i) < 2:
                return "NO"
        return "YES"
    else:
        c, co = 0, 0
        for i in set_s:
            if s.count(i) % 2 != 0:
                c += 1
            if s.count(i) < 2:
                co += 1
        if c % 2 != 0 and co < 2:
            return "YES"
        else:
            return "NO"


if __name__ == "__main__":
    string_to_check = str(input())
    result = check_palindrome(string_to_check)
    print(result)
