def get_precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return 0

def infix_to_postfix(infix_expr):
    stack = []
    postfix_expr = []
    for char in infix_expr:
        if char.isalpha():  # 피연산자인 경우
            postfix_expr.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix_expr.append(stack.pop())
            stack.pop()  # '(' 제거
        else:  # 연산자인 경우
            while stack and get_precedence(stack[-1]) >= get_precedence(char):
                postfix_expr.append(stack.pop())
            stack.append(char)

    while stack:
        postfix_expr.append(stack.pop())

    return ''.join(postfix_expr)

if __name__ == "__main__":
    infix_expression = input().strip()
    postfix_expression = infix_to_postfix(infix_expression)
    print(postfix_expression)
