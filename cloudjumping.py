# Jumping on Clouds

def jump(length, arr):
    count = 0
    cou = 0
    if arr[-1] == 1:
        return "Last cloud is Thunder Cloud"
    else:
        while count != length - 1:
            if count+2 < length and arr[count + 2] == 0:
                count += 2
                cou += 1
            else:
                count += 1
                cou += 1
        return cou


if __name__ == "__main__":
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    r = jump(n, c)
    print(r)
