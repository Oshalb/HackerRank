# Two String

def check_strings(s1, s2):
    s = set(s1).intersection(set(s2))
    if len(s):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        first_string = str(input())
        second_string = str(input())
        result = check_strings(first_string, second_string)
        print(result)
