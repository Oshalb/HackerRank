# Balanced Brackets

def check_braces(s):
    stack = []
    c = len(s)
    if c % 2 != 0:
        return "NO"
    else:
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' or i == ']' or i == '}':
                if len(stack) == 0:
                    return "NO"
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
        if len(stack) == 0:
            return "YES"
        else:
            return "NO"


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        string_to_check = str(input())
        result = check_braces(string_to_check)
        print(result)
