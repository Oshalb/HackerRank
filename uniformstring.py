# Weighted Uniform String
# Less time complexity using dictionary and set
# alpha = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14,
# 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
#
# s = input().strip()
# n = int(input().strip())
# scores = set()
# ctr=1
# for i in range(len(s)):
#     score = alpha[s[i]]
#     ctr = ctr+1 if (i+1 != len(s) and s[i+1] == s[i]) else 1
#     scores.add(score*ctr)
#
# for a0 in range(n):
#     x = int(input().strip())
#     print("Yes" if x in scores else "No")

def calculate_weight(s, q):
    c = ord(s[0]) - 96
    qc = [c]
    ans = []
    count = 0
    for i in range(1, len(s)):
        if (ord(s[i]) - 96) != c:
            c = ord(s[i]) - 96
            qc.append(c)
        else:
            a = qc[-1] + (ord(s[i]) - 96)
            qc.append(a)
    for i in q:
        if i in qc:
            ans.append("Yes")
        else:
            ans.append("No")
    return ans


if __name__ == "__main__":
    string_to_check = str(input())
    queries_to_check = []
    for _ in range(int(input())):
        queries_to_check.append(int(input()))
    result = calculate_weight(string_to_check, queries_to_check)
    print(*result, sep='\n')
