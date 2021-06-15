# Strong Password

def check_password(n, s):
    count = 0
    if not any(i.isdigit() for i in s):
        count += 1
    if not any(i.islower() for i in s):
        count += 1
    if not any(i.isupper() for i in s):
        count += 1
    if not any(i in '!@#$%^&*()-+' for i in s):
        count += 1
    return max(count, 6 - n)


if __name__ == "__main__":
    length_of_password = int(input())
    string_to_check = str(input())
    result = check_password(length_of_password, string_to_check)
    print(result)
