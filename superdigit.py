# Recursive Digit Sum
# n, k = map(int, input().split())
# x = n * k % 9
# print(x if x else 9)

def check_digit(s, n):
    d = []
    for i in s:
        d.append(int(i))
    ds = str(sum(d) * n)
    while len(ds) > 1:
        d = []
        for i in ds:
            d.append(int(i))
        ds = str(sum(d))
    return ds


if __name__ == "__main__":
    number_to_check, number_of_times_to_concatenate = map(int, input().split())
    result = check_digit(str(number_to_check), number_of_times_to_concatenate)
    print(result)
