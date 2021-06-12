# ACM ICPC Team

def count_topics(a, n, m):
    c = []
    for i in range(n):
        for j in range(i+1, n):
            z = bin(int(a[i], 2) | int(a[j], 2)).count('1')
            c.append(z)
    return [max(c), c.count(max(c))]


if __name__ == "__main__":
    number_of_attendees, number_of_topics = map(int, input().split())
    topics_list = []
    for _ in range(number_of_attendees):
        topics_list.append(input())
    result = count_topics(topics_list, number_of_attendees, number_of_topics)
    print(*result, sep="\n")
