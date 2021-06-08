# Mars Exploration

def changed_bits(s):
    n = len(s)
    msg = 'SOS'
    c = 0
    for i in range(0, n-2, 3):
        if msg[0] != s[i]:
            c += 1
        if msg[1] != s[i+1]:
            c += 1
        if msg[2] != s[i+2]:
            c += 1
    return c


if __name__ == "__main__":
    message_string = str(input())
    result = changed_bits(message_string)
    print(result)
