# Running time of Algorithms
import os


def running_time(n, a):
    c = 0
    for i in range(1, n):
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            c += 1
            j -= 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = running_time(num, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
