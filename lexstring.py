# Bigger is Greater

def next_string(s):
    # Find non-increasing suffix
    i = len(s) - 1
    while i > 0 and s[i - 1] >= s[i]:
        i -= 1
    if i <= 0:
        return False

    # Find successor to pivot
    j = len(s) - 1
    while s[j] <= s[i - 1]:
        j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]

    # Reverse suffix
    s[i:] = s[len(s) - 1: i - 1: -1]
    return True


if __name__ == '__main__':
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        strings_to_check = str(input())
        s = list(strings_to_check)
        result = next_string(s)
        if result:
            print(*s, sep="")
        else:
            print("no answer")
