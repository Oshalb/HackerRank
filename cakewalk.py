# Marc's Cakewalk

def calculate_miles(c):
    c.sort(reverse=True)
    r = 0
    for i, a in enumerate(c):
        r += pow(2, i) * a
    return r


if __name__ == "__main__":
    number_of_calories = int(input())
    calories_per_cake = list(map(int, input().rstrip().split()))
    result = calculate_miles(calories_per_cake)
    print(result)
