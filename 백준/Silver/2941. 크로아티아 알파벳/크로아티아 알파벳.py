import re
reg = r'(c=|c-|dz=|d-|lj|nj|s=|z=|[a-z])'
print(len(re.findall(reg,str(input()))))