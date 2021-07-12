# 2D - Array

def max_sum(g):
    m = -99
    for i in range(4):
        for j in range(4):
            s = sum([g[i][j], g[i][j+1], g[i][j+2], g[i+1][j+1],
                     g[i+2][j], g[i+2][j+1], g[i+2][j+2]])
            if s > m:
                m = s
    return m


if __name__ == "__main__":
    grid_to_check = []
    for _ in range(6):
        grid_to_check.append(list(map(int, input().rstrip().split())))
    result = max_sum(grid_to_check)
    print(result)
