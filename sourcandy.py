# Save the Prisoner
# c = (((s - 1 + m - 1) % n) + 1)

def last_prisoner(n, m, s):
    for j in range(m):
        s += 1
        if s == n:
            s = 0
    return s


if __name__ == "__main__":
    number_of_test_cases = int(input())
    for i in range(number_of_test_cases):
        number_of_prisoners, number_of_candy, starting_position = map(int, input().split())
        result = last_prisoner(number_of_prisoners, number_of_candy, starting_position)
        print(result)
