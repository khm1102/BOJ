def abGame(s, t):
    global temp

    if s == t:
        print(1)
        exit(0)
    if len(s) >= len(t):
        return

    if t[-1] == 'A':
        temp = t[:-1]
        abGame(s, temp)

    if t[0] == 'B':
        temp = t[1:]
        temp = temp[::-1]
        abGame(s, temp)

if __name__ == "__main__":
    s = input()
    t = input()
    abGame(s, t)
    print(0)
