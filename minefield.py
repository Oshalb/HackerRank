# The Bomberman Game

def check_mines(r, c, n, f):
    g = [['9' for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            g[i][j] = f[i][j]
    if n % 2 == 0:
        z = ['O' * c for _ in range(r)]
        # print(1)
        return z
    elif n == 1:
        # print(2)
        return g
    else:
        for k in range(2):
            for i in range(r):
                for j in range(c):
                    if g[i][j] == 'O':
                        g[i][j] = '1'
                        if i + 1 < r and g[i + 1][j] != 'O':
                            g[i + 1][j] = '1'
                        if i - 1 > -1 and g[i - 1][j] != 'O':
                            g[i - 1][j] = '1'
                        if j + 1 < c and g[i][j + 1] != 'O':
                            g[i][j + 1] = '1'
                        if j - 1 > -1 and g[i][j - 1] != 'O':
                            g[i][j - 1] = '1'
            for i in range(r):
                for j in range(c):
                    if g[i][j] == '1':
                        g[i][j] = '.'
                    elif g[i][j] == '.':
                        g[i][j] = 'O'
        return g


if __name__ == "__main__":
    rows_of_field, column_of_field, number_of_seconds = map(int, input().rstrip().split())
    field_of_bomb = []
    for _ in range(rows_of_field):
        field_of_bomb.append(str(input()))
    result = check_mines(rows_of_field, column_of_field, number_of_seconds, field_of_bomb)
    for y in result:
        print(*y, sep='')
