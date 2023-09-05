def explode_string(s, bomb):
    stack = []
    last_char = bomb[-1]
    for char in s:
        stack.append(char)
        if char == last_char and ''.join(stack[-len(bomb):]) == bomb:
            del stack[-len(bomb):]
    
    return ''.join(stack)

if __name__ == "__main__":
    string = input().strip()
    bomb = input().strip()
    result = explode_string(string, bomb)
    if result:
        print(result)
    else:
        print("FRULA")
