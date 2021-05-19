if __name__ == "__main__":
    for i in range(int(input())):
        x, y, z = map(int, input().rstrip().split())
        a = abs(x - z)
        b = abs(y - z)

        print("Cat A" if a < b else "Cat B" if b < a else "Mouse C")
