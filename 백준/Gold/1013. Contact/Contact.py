import re

def f(input_str):
    pattern = r'(100+1+|01)+'
    return re.fullmatch(pattern, input_str) is not None

T = int(input())
for _ in range(T):
    str = input()
    if f(str):print("YES")
    else:print("NO")