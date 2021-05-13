if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    r = []
    for grade in grades:
        diff = 5 - grade % 5
        if grade >= 38 and diff < 3:
            grade += diff
        r.append(grade)
    print(*r, sep='\n')