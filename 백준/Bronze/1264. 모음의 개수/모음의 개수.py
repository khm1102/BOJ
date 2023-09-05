vowels = 'aeiouAEIOU'
while True:
    line = input()
    if line == '#':
        break
    vowel_count = 0
    for char in line:
        if char in vowels:
            vowel_count += 1
    print(vowel_count)