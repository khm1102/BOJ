import sys


input = sys.stdin.readline
print = sys.stdout.write

dq = []


n = int(input())


for _ in range(n):
    command = input().split()

    if command[0] == 'push_front':
        dq.insert(0, int(command[1]))
    elif command[0] == 'push_back':
        dq.append(int(command[1]))
    elif command[0] == 'pop_front':
        if dq:
            print(str(dq.pop(0)) + '\n')
        else:
            print('-1\n')
    elif command[0] == 'pop_back':
        if dq:
            print(str(dq.pop()) + '\n')
        else:
            print('-1\n')
    elif command[0] == 'size':
        print(str(len(dq)) + '\n')
    elif command[0] == 'empty':
        if dq:
            print('0\n')
        else:
            print('1\n')
    elif command[0] == 'front':
        if dq:
            print(str(dq[0]) + '\n')
        else:
            print('-1\n')
    elif command[0] == 'back':
        if dq:
            print(str(dq[-1]) + '\n')
        else:
            print('-1\n')