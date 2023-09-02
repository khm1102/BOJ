def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            else:
                stack.pop()
    return len(stack) == 0