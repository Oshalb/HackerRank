# Caesar Cipher

def encrypt_text(s, n):
    c = ""
    for i in s:
        if ord(i) in range(65, 91):
            c += chr((ord(i) + n - 65) % 26 + 65)
        elif ord(i) in range(97, 123):
            c += chr((ord(i) + n - 97) % 26 + 97)
        else:
            c += i
    return c


if __name__ == "__main__":
    length_of_string = int(input())
    string_to_encrypt = str(input())
    number_to_rotate = int(input())
    result = encrypt_text(string_to_encrypt, number_to_rotate)
    print(result)
