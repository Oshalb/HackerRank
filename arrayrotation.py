# Circular Array Rotation

if __name__ == "__main__":
    number_of_integer, rotation_count, number_of_queries = map(int, input().split())
    arr = list(map(int, input().rstrip().split()))
    queries = list(map(int, input().rstrip().split()))
    for i in queries:
        rotation_count %= number_of_integer
        print(arr[i-rotation_count])
