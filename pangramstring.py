# Pangrams

def check_pangram(s):
    s = s.lower()
    c = 0
    for i in range(97, 123):
        if chr(i) in s:
            c += 1
    return 'pangram' if c == 26 else 'not pangram'


if __name__ == "__main__":
    string_to_check = str(input())
    result = check_pangram(string_to_check)
    print(result)
