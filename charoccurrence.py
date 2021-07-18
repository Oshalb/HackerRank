# Sherlock and the Valid String

def check_string(s):
    set_s = set(s)
    length_of_characters = {}
    for i in set_s:
        lc = s.count(i)
        if lc not in length_of_characters:
            length_of_characters[lc] = [i]
        else:
            length_of_characters[lc].append(i)
    llc = len(length_of_characters)
    s = [i for i in length_of_characters]
    if llc > 2:
        return "NO"
    else:
        if llc == 1:
            return "YES"
        else:
            if 1 in length_of_characters:
                if len(length_of_characters[1]) == 1:
                    return "YES"
            if abs(s[0] - s[1]) > 1:
                return "NO"
            else:
                if len(length_of_characters[max(s)]) != 1:
                    return "NO"
                else:
                    return "YES"


if __name__ == "__main__":
    string_to_check = str(input())
    result = check_string(string_to_check)
    print(result)
