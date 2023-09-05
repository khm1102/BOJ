n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

df = end - n
if line%2 == 0: 
    top = line - df
    bt = df + 1
else:
    top = df + 1 
    bt = line - df

print("%d/%d"%(top,bt))
