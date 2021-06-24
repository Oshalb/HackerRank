# Beautiful Binary String

def count_string(s):
    c = 0
    i, j = 1, len(s)-1
    while i < j:
        if s[i] == '1':
            if s[i - 1] == s[i + 1] == '0':
                c += 1
                i += 3
            else:
                i += 1
        else:
            i += 1
    return c


if __name__ == "__main__":
    length_of_string = int(input())
    string_to_check = list(str(input()))
    result = count_string(string_to_check)
    print(result)
