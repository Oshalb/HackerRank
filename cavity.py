# Cavity Map

def check_cavity(g, n):
    g2d = [[0 for i in range(n)] for j in range(n)]
    z, k = [], []
    for i in range(n):
        for j in range(n):
            g2d[i][j] = int(g[i][j])
    for i in range(1, (n - 1)):
        for j in range(1, (n - 1)):
            if g2d[i][j] > max(g2d[i - 1][j], g2d[i + 1][j], g2d[i][j - 1], g2d[i][j + 1]):
                z.append(i)
                k.append(j)
    for i in range(len(z)):
        g2d[z[i]][k[i]] = 'X'
    return g2d


if __name__ == "__main__":
    number = int(input())
    grid = []
    for _ in range(number):
        grid_item = input()
        grid.append(grid_item)
    result = check_cavity(grid, number)
    for row in result:
        print(*row, sep='')
