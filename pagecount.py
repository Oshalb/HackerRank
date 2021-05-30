# Drawing Book
# def pageCount(n, p):
#     if not n%2:
#         n += 1
#     return min(p//2, (n-p)//2)

def count_pages(n, p):
    if p % 2 == 0:
        f = int(p / 2)
        if n % 2 == 0:
            b = int((n - p) / 2)
        else:
            b = int(((n - p) - 1) / 2)
        return f if f < b else b
    else:
        f = int((p - 1) / 2)
        if n % 2 == 0:
            b = int(((n - p) + 1) / 2)
        else:
            b = int((n - p) / 2)
        return f if f < b else b


if __name__ == "__main__":
    no_of_pages = int(input())
    pages_to_turn = int(input())
    result = count_pages(no_of_pages,  pages_to_turn)
    print(result)
