# Luck Balance

def count_luck(d, k):
    total = sum(d[0])
    d[1].sort()
    a = len(d[1]) - k
    if a < 0:
        a = 0
    total += sum(d[1][a:])
    total -= sum(d[1][:a])
    return total


if __name__ == "__main__":
    number_of_contest, max_contest_to_lose = map(int, input().rstrip().split())
    dictionary_of_contest = {0: [], 1: []}
    for _ in range(number_of_contest):
        luck_value, contest_importance = map(int, input().rstrip().split())
        if contest_importance == 1:
            dictionary_of_contest[1].append(luck_value)
        elif contest_importance == 0:
            dictionary_of_contest[0].append(luck_value)
    result = count_luck(dictionary_of_contest, max_contest_to_lose)
    print(result)
