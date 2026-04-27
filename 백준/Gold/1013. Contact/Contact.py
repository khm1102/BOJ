import re

def check_pattern(input_str):
    pattern = r'(100+1+|01)+'
    return re.fullmatch(pattern, input_str) is not None

T = int(input())

for _ in range(T):
    test_str = input()
    if check_pattern(test_str):
        print("YES")
    else:
        print("NO")
