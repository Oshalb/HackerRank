# HackerRank in a String

def check_string(q):
    z = 'hackerrank'
    c = 0
    for i in q:
        if i == z[c]:
            c += 1
    return "YES" if c == 9 else "NO"


if __name__ == "__main__":
    number_of_queries = int(input())
    queries = []
    for _ in range(number_of_queries):
        queries.append(input())
    result = check_string(queries)
    print(result)
