# Sherlock and the Valid String

def check_string(s):
    # unique letters in the string
    set_s = set(s)
    # counting the length of each character in the string as length: [character]
    length_of_characters = {}
    for i in set_s:
        lc = s.count(i)
        if lc not in length_of_characters:
            length_of_characters[lc] = [i]
        else:
            length_of_characters[lc].append(i)
    llc = len(length_of_characters)
    s = [i for i in length_of_characters]
    # checking if there are more than 2 lengths of characters
    if llc > 2:
        return "NO"
    else:
        # check if there if only one length and return
        if llc == 1:
            return "YES"
        else:
            # check if any character only occurs once, if it does return
            if 1 in length_of_characters:
                if len(length_of_characters[1]) == 1:
                    return "YES"
            # check if difference if length between two characters is more than one, if ture then return
            if abs(s[0] - s[1]) > 1:
                return "NO"
            else:
                # if difference is less than 2, then check if the number of characters in
                # the max length if more than 1, if true then return
                if len(length_of_characters[max(s)]) != 1:
                    return "NO"
                # if false return
                else:
                    return "YES"


if __name__ == "__main__":
    string_to_check = str(input())
    result = check_string(string_to_check)
    print(result)
