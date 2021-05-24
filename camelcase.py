import re

if __name__ == "__main__":
    s = input()
    s = s = re.split('(?=[A-Z])', s)

    print(len(s))
