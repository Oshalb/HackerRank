# The Full Counting Sort

def string_counting_sort(d):
    r = ""
    set_s = {i for i in d}
    set_s = sorted(set_s)
    for i in set_s:
        for j in d[i]:
            r += j
            r += ' '
    return r


if __name__ == "__main__":
    number_of_pairs = int(input())
    dictonary_of_pairs = {}
    number_of_strings = number_of_pairs//2
    for _ in range(number_of_strings):
        inp1, inp2 = input().rstrip().split()
        y = int(inp1)
        z = str(inp2)
        if y not in dictonary_of_pairs:
            dictonary_of_pairs[y] = ['-']
        else:
            dictonary_of_pairs[y].append('-')
    for _ in range(number_of_strings, number_of_pairs):
        inp1, inp2 = input().rstrip().split()
        y = int(inp1)
        z = str(inp2)
        if y not in dictonary_of_pairs:
            dictonary_of_pairs[y] = [z]
        else:
            dictonary_of_pairs[y].append(z)
    result = string_counting_sort(dictonary_of_pairs)
    print(result)
