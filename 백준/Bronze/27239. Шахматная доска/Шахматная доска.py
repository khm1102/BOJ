n = int(input())

row = (n-1) // 8 + 1
col = (n-1) %  8

print(f"{chr(ord('a')+col)}{row}")