n = int(input())  
cards = list(map(int, input().split()))  
m = int(input())  
targets = list(map(int, input().split()))  
counts = {} 
for card in cards:
    if card in counts:
        counts[card] += 1
    else:
        counts[card] = 1
for target in targets:
    if target in counts:
        print(counts[target], end=' ')
    else:
        print(0, end=' ')
