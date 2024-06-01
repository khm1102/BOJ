import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:n+1]))

    a.sort(reverse=True)

    for num in a:
        print(num)

if __name__ == "__main__":
    main()
