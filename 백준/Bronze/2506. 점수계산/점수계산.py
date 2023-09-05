N = int(input())
answers = list(map(int, input().split()))

score = 0 
bonus = 0  

for answer in answers:
    if answer == 1:
        bonus += 1
        score += bonus
    else:
        bonus = 0

print(score)
