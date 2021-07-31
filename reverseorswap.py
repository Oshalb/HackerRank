# Almost Sorted

def check_sorted(a):
    i, j = 0, 1
    while j < len(a):
        if a[i] > a[j]:
            return False
        else:
            i += 1
            j += 1
    return True


def find_indices(a):
    large, small = 0, 0
    for i in range(1, len(a)-1):
        if a[i-1] < a[i] > a[i+1]:
            large += 1
            r.append(i)
        elif a[i-1] > a[i] < a[i+1]:
            small += 1
            r.append(i)


def swap_and_check(b):
    temp = [y for y in b]
    temp[r[0]], temp[r[-1]] = temp[r[-1]], temp[r[0]]
    if check_sorted(temp):
        return True
    else:
        return False


def reverse_and_check(c):
    temp = c[:r[0]] + c[r[1]:r[0]-1:-1] + c[r[1]+1:]
    if check_sorted(temp):
        return True
    else:
        return False


def main():
    size_of_list = int(input())
    list_to_check = list(map(int, input().rstrip().split()))
    list_to_check.insert(0, float('-inf'))
    list_to_check.append(float('inf'))
    if check_sorted(list_to_check):
        print("yes")
        return True
    else:
        find_indices(list_to_check)
        if len(r) == 2:
            if swap_and_check(list_to_check):
                print("yes")
                print("swap", *r, sep=' ')
                return True
            else:
                if reverse_and_check(list_to_check):
                    print("yes")
                    print("reverse", *r, sep=' ')
                    return True
                else:
                    print("no")
                    return True
        else:
            if swap_and_check(list_to_check):
                print("yes")
                print("swap", r[0], r[-1])
                return True
            else:
                print("no")
                return True


if __name__ == "__main__":
    r = []
    main()
