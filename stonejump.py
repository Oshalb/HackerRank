# Manasa and Stones

def count_last_stones(n, a, b):
    r = [0, 0]
    r[0] = n * a
    r[1] = n * b
    r = sorted(r)
    return r


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        number_of_stones = int(input())
        first_difference = int(input())
        second_difference = int(input())
        result = count_last_stones(number_of_stones - 1, first_difference, second_difference)
        f, s, d = result[0], result[1], abs(second_difference - first_difference)
        if d == 0:
            print(f)
        else:
            print(*range(f, s+d, d))
