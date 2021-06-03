# Fair Rations

def calculate_bread(n, b):
    c = 0
    oc = len([num for num in b if num % 2 != 0])
    if oc % 2 != 0:
        return "NO"
    else:
        for i in range(n-1):
            if b[i] % 2 != 0:
                b[i] += 1
                b[i+1] += 1
                c += 2
        return c


if __name__ == "__main__":
    number_of_subjects = int(input())
    breads_owned_by_subjects = list(map(int, input().rstrip().split()))
    result = calculate_bread(number_of_subjects, breads_owned_by_subjects)
    print(result)
