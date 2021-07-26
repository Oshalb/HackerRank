# The Bomberman Game
# Optimized time

def minefield(g, n, r, c):
    grid = [['0' for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            grid[i][j] = g[i][j]
    for k in range(n):
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'O':
                    grid[i][j] = '1'
                    if i + 1 < r and grid[i + 1][j] != 'O':
                        grid[i + 1][j] = '1'
                    if i - 1 > -1 and grid[i - 1][j] != 'O':
                        grid[i - 1][j] = '1'
                    if j + 1 < c and grid[i][j + 1] != 'O':
                        grid[i][j + 1] = '1'
                    if j - 1 > -1 and g[i][j - 1] != 'O':
                        grid[i][j - 1] = '1'
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    grid[i][j] = '.'
                elif grid[i][j] == '.':
                    grid[i][j] = 'O'
    return grid


def main():
    number_of_rows, number_of_columns, number_of_seconds = map(int, input().rstrip().split())
    grid_to_check = []
    for _ in range(number_of_rows):
        grid_to_check.append(str(input()))
    if number_of_seconds == 1:
        for y in grid_to_check:
            print(*y, sep='')
    elif number_of_seconds % 2 == 0:
        for y in range(number_of_rows):
            for k in range(number_of_columns):
                print('O', end='')
            print()
    elif (number_of_seconds - 3) % 4 == 0:
        result = minefield(grid_to_check, 1, number_of_rows, number_of_columns)
        for y in result:
            print(*y, sep='')
    elif (number_of_seconds - 1) % 4 == 0:
        result = minefield(grid_to_check, 2, number_of_rows, number_of_columns)
        for y in result:
            print(*y, sep='')


if __name__ == "__main__":
    main()
