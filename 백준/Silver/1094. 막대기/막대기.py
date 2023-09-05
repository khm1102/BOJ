X = int(input())
sticks = [64]

while sum(sticks) > X:
    shortest = min(sticks)
    sticks.remove(shortest)
    sticks += [shortest//2] * 2
    if sum(sticks[:-1]) >= X:
        sticks.pop()

print(len(sticks))
