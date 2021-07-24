# Frequency Queries

def operaiton_on_value(q):
    r = []
    for x in q:
        o, v = x[0], x[1]
        if o == 1:
            if v not in dictonary_of_values:
                dictonary_of_values[v] = 1
            else:
                dictonary_of_values[v] += 1
        elif o == 2:
            if v in dictonary_of_values:
                if dictonary_of_values[v] > 0:
                    dictonary_of_values[v] -= 1
        elif o == 3:
            r.append(1 if v in set(dictonary_of_values.values()) else 0)
    return r


if __name__ == "__main__":
    number_of_queries = int(input())
    dictonary_of_values = {}
    queries_to_do = []
    for _ in range(number_of_queries):
        queries_to_do.append(list(map(int, input().rstrip().split())))
    result = operaiton_on_value(queries_to_do)
    print(*result, sep="\n")
