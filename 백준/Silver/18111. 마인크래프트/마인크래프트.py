N, M, B = map(int, input().split())
terrain = []
for _ in range(N):
    terrain.extend(list(map(int, input().split())))

min_time = float('inf')  
max_height = 0  

for height in range(257):
    blocks_removed = 0
    blocks_added = 0  


    for block in terrain:
        if block > height:
            blocks_removed += block - height

    for block in terrain:
        if block < height:
            blocks_added += height - block

    time = blocks_removed * 2 + blocks_added

    if B + blocks_removed >= blocks_added:
        if time <= min_time:
            min_time = time
            max_height = height

print(min_time, max_height)
