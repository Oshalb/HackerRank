# Happy Ladybug

def check_colours(n, s):
    for a in set(s):
        if a != "_" and s.count(a) == 1:
            return "NO"

    if s.count("_") == 0:
        for i in range(1, n - 1):
            if s[i - 1] != s[i] and s[i + 1] != s[i]:
                return "NO"
    return "YES"


if __name__ == "__main__":
    number_of_games = int(input())
    for _ in range(number_of_games):
        number_of_cells = int(input())
        cell_positions = str(input())
        result = check_colours(number_of_cells, cell_positions)
        print(result)
