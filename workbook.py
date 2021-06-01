# Lisa's Workbook

def count_special_problems(k, arr):
    pages = []
    for i in arr:
        for j in range(0, i+1):
            pages.append(j)
    page = 0
    lp = len(pages)
    c, b = 0, 0
    for i in range(lp):
        if b == k or pages[i] == 1:
            b = 0
            page += 1
        b += 1
        if pages[i] == page:
            c += 1
    return c


if __name__ == "__main__":
    number_of_chapters = int(input())
    number_of_problems = int(input())
    problems_per_chapter_array = list(map(int, input().rstrip().split()))
    result = count_special_problems(number_of_problems, problems_per_chapter_array)
    print(result)
