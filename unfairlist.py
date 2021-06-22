# Min Max

def check_list(a, k):
    a.sort()
    la = len(a)
    m = 9999999999
    for i in range(la):
        if k+i-1 >= la:
            break
        else:
            z = a[k+i-1] - a[i]
        if z < m:
            m = z
    return m


if __name__ == "__main__":
    length_of_list = int(input())
    length_of_fair_list = int(input())
    unfair_list = []
    for _ in range(length_of_list):
        unfair_list.append(int(input()))
    result = check_list(unfair_list, length_of_fair_list)
    print(result)
