# Flipping bits

def flip_bits(n):
    # Output of bin has 0b attached at the start
    b = bin(n)
    b = b.replace("0b", '')
    length_of_b = len(b)
    zeros_to_add = 32 - length_of_b
    string_of_zero = '0' * zeros_to_add
    c = string_of_zero + b
    c = c.replace('1', '2')
    c = c.replace('0', '1')
    c = c.replace('2', '0')
    return int(c, 2)


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        number_to_change = int(input())
        result = flip_bits(number_to_change)
        print(result)
