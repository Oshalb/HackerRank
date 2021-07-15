# Hash Tables: Ransom Note

def check_words(m, n):
    c = 0
    for i in n:
        if i in m:
            if n[i] <= m[i]:
                c += 1
    if c == len(n):
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    number_of_words_in_magazine, number_of_words_in_note = map(int, input().rstrip().split())

    words_in_magazine = {}
    for k in map(str, input().rstrip().split()):
        if k not in words_in_magazine:
            words_in_magazine[k] = 1
        else:
            words_in_magazine[k] += 1

    words_in_note = {}
    for k in map(str, input().rstrip().split()):
        if k not in words_in_note:
            words_in_note[k] = 1
        else:
            words_in_note[k] += 1

    result = check_words(words_in_magazine, words_in_note)
    print(result)
