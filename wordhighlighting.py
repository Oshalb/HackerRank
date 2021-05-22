if __name__ == "__main__":
    h = list(map(int, input().rstrip().split()))
    word = input()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lw, la = len(word), len(alphabet)
    wordtonum = []
    for i in range(lw):
        for j in range(la):
            if word[i] == alphabet[j]:
                wordtonum.append(j)
    m = h[wordtonum[0]]
    for i in range(1, lw):
        if h[wordtonum[i]] > m:
            m = h[wordtonum[i]]
    print(m * lw)
