# Library Fine

def calculate_fine(rd, dd):
    fine = 0
    if rd[2] > dd[2]:
        fine = 10000
    elif rd[2] < dd[2]:
        fine = 0
    else:
        if rd[1] > dd[1]:
            fine = (rd[1] - dd[1]) * 500
        elif rd[1] < dd[1]:
            fine = 0
        else:
            if rd[0] > dd[0]:
                fine = (abs(rd[0] - dd[0])) * 15
            elif rd[0] < dd[0]:
                fine = 0
    return fine


if __name__ == "__main__":
    return_date = list(map(int, input().rstrip().split()))
    due_date = list(map(int, input().rstrip().split()))
    result = calculate_fine(return_date, due_date)
    print(result)
