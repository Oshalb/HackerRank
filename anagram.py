# Making Anagrams

def check_anagram(s1, s2):
    a = set(s1).intersection(s2)
    b, c = 0, 0
    for i in a:
        b += min(s1.count(i), s2.count(i))
    r = abs((b*2) - (len(s1)+len(s2)))
    return r


if __name__ == "__main__":
    first_string = str(input())
    second_string = str(input())
    result = check_anagram(first_string, second_string)
    print(result)
