import sys
from collections import deque

def process_commands(command_list, num_list):
    reverse = False

    for command in command_list:
        if command == "R":
            reverse = not reverse
        else:
            if num_list:
                if reverse:
                    num_list.pop()
                else:
                    num_list.popleft()
            else:
                return "error"

    return num_list if not reverse else reversed(num_list)

def main():
    test_cases = int(sys.stdin.readline())

    for _ in range(test_cases):
        command_list = sys.stdin.readline().strip()
        num_cnt = int(sys.stdin.readline())
        num_list = deque(sys.stdin.readline().strip()[1:-1].split(","))

        if num_cnt == 0:
            num_list = deque()

        result = process_commands(command_list, num_list)
        if result == "error":
            print("error")
        else:
            print(f"[{','.join(result)}]")

if __name__ == "__main__":
    main()
