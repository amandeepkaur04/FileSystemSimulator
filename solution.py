def solution(s):

    if s == "":
        return 1

    l = len(s)
    if l % 2 != 0:
        return 0

    stack = []

    for c in s:
        if c in ["(", "{", "["]:
            stack.append(c)

        elif c in ["]", "}",")"]:
            if len(stack) == 0:
                return 0
            p = stack.pop()
            if c == ')' and p != '(':
                return 0
            elif c == ']' and p != '[':
                return 0
            elif c == '}' and p != '{':
                return 0

    return 1


if __name__ == "__main__":

    test_set = [
        "{[()()]}",
        "([)()]",
        "",
        "[",
        "[])",
    ]

    for test_string in test_set:
        if solution(test_string):
            print("{}: properly nested".format(test_string))
        else:
            print("{}: NOT properly nested".format(test_string))