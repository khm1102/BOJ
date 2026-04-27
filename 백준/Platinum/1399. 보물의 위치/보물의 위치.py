def dig(x):
    return x if x < 10 else dig(sum(map(int, str(x))))

def main():
    t = int(input())
    for _ in range(t):
        k, m = map(int, input().split())
        x, y, direction = 0, 0, 0
        visited = [0] * 10
        num = 1
        q = []
        while k > 0:
            if visited[num]:
                q = q[q.index(num):]
                k %= (4 * len(q))
                if k == 0:
                    break
            visited[num] = 1
            q.append(num)
            x += [0, num, 0, -num][direction]
            y += [num, 0, -num, 0][direction]
            k, num, direction = k - 1, dig(num * m), (direction + 1) % 4
        print(x, y)

if __name__ == "__main__":
    main()
