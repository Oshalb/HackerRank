# Two Character

def check_alternate_letters(s):
    ss = []
    for i in s:
        if i not in ss:
            ss.append(i)
    lss = len(ss)
    max_alt_string = [0]
    for i in range(lss - 1):
        for j in range(i + 1, lss):
            c = 0
            for k in s:
                if ss[i] == k:
                    c += 1
                elif ss[j] == k:
                    c -= 1
                if c == -1 or c == 2:
                    break
            if c == 0 or c == 1:
                max_alt_string.append(s.count(ss[i]) + s.count(ss[j]))
    return max(max_alt_string)


if __name__ == "__main__":
    length_of_string = int(input())
    string_to_check = str(input())
    result = check_alternate_letters(string_to_check)
    print(result)
