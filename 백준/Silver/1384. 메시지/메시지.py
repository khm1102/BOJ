def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    group_num = 0
    index = 0

    while index < len(data):
        n = int(data[index])
        if n == 0:
            break

        group_num += 1
        names = []
        messages = []

        for i in range(n):
            line = data[index + 1 + i].split()
            names.append(line[0])
            messages.append(line[1:])

        index += n + 1

        nasty_comments = []

        for i in range(n):
            for j in range(n - 1):
                if messages[i][j] == 'N':
                    target_index = (i - j - 1) % n
                    nasty_comments.append((names[(i - j - 1) % n], names[i]))

        print(f"Group {group_num}")

        if nasty_comments:
            for comment in nasty_comments:
                print(f"{comment[0]} was nasty about {comment[1]}")
        else:
            print("Nobody was nasty")

        print()  

if __name__ == "__main__":
    main()
