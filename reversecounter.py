# Strange Counter

def check_counter(t):
    rem = 3
    while t > rem:
        t = t - rem
        rem *= 2
    return rem - t + 1


if __name__ == "__main__":
    time_to_check = int(input())
    result = check_counter(time_to_check)
    print(result)
