def dig(x):
    if x < 10:
        return x
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return dig(sum)

def main():
    t = int(input())
    for _ in range(t):
        k, m = map(int, input().split())
        x = y = 0
        dir = 0
        visited = [0] * 10
        num = 1
        q = []
        while k > 0:
            if visited[num]:
                while q[0] != num:
                    q.pop(0)
                k %= (4 * len(q))
                if k == 0:
                    break
            visited[num] = 1
            q.append(num)
            if dir == 0:
                y += num
            elif dir == 1:
                x += num
            elif dir == 2:
                y -= num
            elif dir == 3:
                x -= num
            k -= 1
            num = dig(num * m)
            dir = (dir + 1) % 4
        print(x, y)

if __name__ == "__main__":
    main()
