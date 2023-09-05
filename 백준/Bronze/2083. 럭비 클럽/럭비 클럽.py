while True:
    line = input().split()
    name = line[0]
    age = int(line[1])
    weight = int(line[2])
    
    if name == '#' and age == 0 and weight == 0:
        break
    
    if age > 17 or weight >= 80:
        category = 'Senior'
    else:
        category = 'Junior'
    
    print(name, category)
