# Arrays: Left Rotation

def rotate_list(a, n, d):
    c = d % n
    r = a[c:] + a[:c]
    return r


if __name__ == "__main__":
    size_of_list, number_of_rotation = map(int, input().rstrip().split())
    list_to_rotate = list(map(int, input().rstrip().split()))
    result = rotate_list(list_to_rotate, size_of_list, number_of_rotation)
    print(*result, sep=' ')
