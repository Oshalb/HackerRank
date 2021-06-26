# 3D Surface Area


def get_surface_area(a, h, w):
    sa = h * w * 2
    for i in [a, zip(*a)]:
        for r in i:
            last_height = 0
            valley = 0
            sa += max(r) * 2
            for c in r:
                if c < last_height:
                    valley += last_height - c
                elif c > last_height and valley:
                    diff = min([valley, c - last_height])
                    valley -= diff
                    sa += diff * 2
                last_height = c
    return sa


if __name__ == "__main__":
    height_of_board, width_of_board = map(int, input().rstrip().split())
    blocks_on_board = []
    for _ in range(height_of_board):
        blocks_on_board.append(list(map(int, input().rstrip().split())))
    result = get_surface_area(blocks_on_board, height_of_board, width_of_board)
    print(result)
