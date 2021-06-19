# Separate Two Numbers

def check_numbers(s):
    if s[0] == '0' and s[1] != '1':
        return "NO"
    else:
        loop = int(len(s) / 2)
        first_numbers = []
        for i in range(1, loop+1):
            first_numbers.append(s[0:i])
        for i in first_numbers:
            k = ""
            f = i
            k += str(f)
            while len(k) < len(s):
                f += 1
                k += str(f)
            if s == k:
                return "YES " + str(i)
        return "NO"


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        result = check_numbers(str(input()))
        print(result)
