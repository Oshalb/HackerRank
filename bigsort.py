# Big Sorting

if __name__ == "__main__":
    length_of_list = int(input())
    list_in_dictionary = {}
    for _ in range(length_of_list):
        x = input()
        try:
            list_in_dictionary[len(x)].append(x)
        except KeyError:
            list_in_dictionary[len(x)] = [x]
    for i in sorted(list_in_dictionary):
        for j in sorted(list_in_dictionary[i]):
            print(j)
