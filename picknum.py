# Picking Numbers

# if __name__ == "__main__":
#     n = int(input())
#     arr = list(map(int, input().split()))
#     a = list(set(arr))
#     al = len(a)
#     f = []
#     for i in range(al-1):
#         if abs(a[i] - a[i+1]) <= 1:
#             f.append(a[i])
#             f.append(a[i+1])
#     fl = len(f)
#     c = 0
#     # print(a, f)
#     for i in range(0, fl, 2):
#         cou = 0
#         if i + 1 < fl:
#             cou += arr.count(f[i]) + arr.count(f[i+1])
#             # print(cou, i, i+1, arr.count(97), arr.count(4), len(arr))
#         if cou >= c:
#             c = cou
#     # m = 0
#     # for i in a:
#     #     cm = 0
#     #     cm = arr.count(i)
#     #     if cm > m:
#     #         m = cm
#     if al == 1:
#         c = n
#     # elif m < c:
#     #     c = m
#     print(c)
if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().split()]
    maximum = 0
    for i in arr:
        c = arr.count(i)
        d = arr.count(i-1)
        c = c+d
        if c > maximum:
            maximum = c
    print(maximum)
