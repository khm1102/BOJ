class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.s = []

    def calculate_sides(self):
        for i in range(4):
            for j in range(i + 1, 4):
                self.s.append((self.x[i] - self.x[j]) ** 2 + (self.y[i] - self.y[j]) ** 2)

        self.s.sort()

    def is_rectangle(self):
        return int(self.s[0] == self.s[1] == self.s[2] == self.s[3] and self.s[4] == self.s[5])


if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        x = []
        y = []
        for i in range(4):
            x_i, y_i = map(int, input().split())
            x.append(x_i)
            y.append(y_i)

        rectangle = Rectangle(x, y)
        rectangle.calculate_sides()
        print(rectangle.is_rectangle())
