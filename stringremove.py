# Super Reduced String

def reduced_string(s):
    ss = list(s)
    i = 0
    while i < len(ss)-1:
        if ss[i] == ss[i+1]:
            del ss[i+1]
            del ss[i]
            i = 0
        else:
            i += 1
    if len(ss) == 0:
        return "Empty String"
    else:
        print(*ss, sep="")


if __name__ == "__main__":
    string_to_check = str(input())
    result = reduced_string(string_to_check)
    if result:
        print(result)
