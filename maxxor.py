# Maximising XOR


def find_max(n, m):
    max_xor = 0
    for i in range(n, m + 1):
        for j in range(n, m + 1):
            if i ^ j > max_xor:
                max_xor = i ^ j
    return max_xor


if __name__ == "__main__":
    first_number = int(input())
    second_number = int(input())
    result = find_max(first_number, second_number)
    print(result)
