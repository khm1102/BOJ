def is_balanced_string(s):
    stack = []
    for char in s:
        if char in ['(', '[']:
            stack.append(char)
        elif char in [')', ']']:
            if not stack:
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or (char == ']' and top != '['):
                return False
    return len(stack) == 0

while True:
    string = input()
    if string == '.':
        break
    if is_balanced_string(string):
        print("yes")
    else:
        print("no")
