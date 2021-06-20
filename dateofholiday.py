# Day of the Programmer

def find_date(y):
    if y == 1918:
        return "26.09." + str(y)
    elif y in range(1700, 1918):
        if y % 4 == 0:
            return "12.09." + str(y)
        else:
            return "13.09." + str(y)
    elif y in range(1919, 2701):
        if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
            return "12.09." + str(y)
        else:
            return "13.09." + str(y)
    else:
        return"Year Not in Range"


if __name__ == "__main__":
    year_to_check = int(input())
    result = find_date(year_to_check)
    print(result)
