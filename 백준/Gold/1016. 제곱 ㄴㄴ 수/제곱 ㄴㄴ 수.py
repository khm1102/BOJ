mn , mx = map(int,input().split())
num = [True] * (mx - mn +1)
# print(num)

for i in range(2, int(mx ** 0.5) + 1):
    temp = i * i
    index = (mn // temp) * temp

    if index < mn:
        index += temp
    for j in range(index, mx +1 , temp):
        num[j -mn] =False

print(sum(num))