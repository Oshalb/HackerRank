# Sum vs XOR

def sum_and_xor(n):
    sn = str(n)
    i = sn.count('0')
    c = pow(2, i)
    return c


if __name__ == "__main__":
    number_to_check = int(input())
    result = sum_and_xor(number_to_check)
    print(result)
