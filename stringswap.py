# Append and Delete

def compare_strings(s, t, k):
    c, i = 0, 0
    while (len(s) > i and len(t) > i) and s[i] == t[i]:
        c += 1
        i += 1
    ops = len(s) + len(t)
    if (ops - 2 * c) > k:
        return "No"
    elif (ops - 2 * c) % 2 == k % 2:
        return "Yes"
    elif (ops - k) < 0:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    string_to_change = list(str(input()))
    string_to_compare = list(str(input()))
    number_of_operation = int(input())
    result = compare_strings(string_to_change, string_to_compare, number_of_operation)
    print(result)
