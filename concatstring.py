# String Construction

def transfer_string(s):
    ss = set(s)
    lss = len(ss)
    return lss


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        string_to_use = str(input())
        result = transfer_string(string_to_use)
        print(result)
