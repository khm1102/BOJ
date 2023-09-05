def check_sequence(n, sequence):
    stack = []  
    result = [] 
    current_num = 1  

    for num in sequence:
        while current_num <= num:
            stack.append(current_num)
            result.append('+')
            current_num += 1

        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            return 'NO'
    return '\n'.join(result)
n = int(input())
sequence = []
for _ in range(n):
    sequence.append(int(input()))

answer = check_sequence(n, sequence)
print(answer)
