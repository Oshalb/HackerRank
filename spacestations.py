# Flatland Space Station

def calculate_distance(n, m, c):
    if m == 1:
        if c[0] == 0 or c[0] == n:
            return n - 1
        else:
            first, last = c[0], abs(c[0] - n + 1)
            return max(first, last)
    else:
        c = sorted(c)
        d = 0
        temp = [0, 0]
        min_dis = []
        for i in range(m-1):
            if c[i+1] - c[i] > d:
                temp[0] = c[i]
                temp[1] = c[i+1]
                d = c[i+1] - c[i]
        if d <= 1:
            return 0
        for i in range(temp[0]+1, temp[1]):
            min_dis.append(min(abs(temp[0]-i), abs(temp[1]-i)))
        first, last, m = c[0], abs(c[-1] - n + 1), max(min_dis)
        return max(m, first, last)


if __name__ == "__main__":
    number_of_cities, number_of_stations = map(int, input().split())
    station_location = list(map(int, input().rstrip().split()))
    result = calculate_distance(number_of_cities, number_of_stations, station_location)
    print(result)
