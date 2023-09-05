N = int(input())
a = 10

while N > a:
    
  if N % a >= a // 2:
    N += a
    
    
  N -= (N % a)
  a *= 10
print(N)