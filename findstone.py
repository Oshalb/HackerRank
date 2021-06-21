# Gemstone

def calculate_gemstones(s):
    ls = len(s)
    r = 0
    for i in s[0]:
        c = 0
        for j in range(ls):
            if i in s[j]:
                c += 1
        if c == ls:
            r += 1
    return r


if __name__ == "__main__":
    number_of_string = int(input())
    list_of_minerals = []
    for _ in range(number_of_string):
        list_of_minerals.append(str(input()))
    result = calculate_gemstones(list_of_minerals)
    print(result)
