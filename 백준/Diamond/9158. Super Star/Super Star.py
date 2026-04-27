import math

class f:
    def __init__(self):
        self.points = []
        self.x = 0
        self.y = 0
        self.z = 0
        self.r = 0.1

    def euclidean(self, x1, y1, z1, x2, y2, z2):
        return math.hypot(x1 - x2, y1 - y2, z1 - z2)

    def update(self, point):
        self.x += (point[0] - self.x) * self.r
        self.y += (point[1] - self.y) * self.r
        self.z += (point[2] - self.z) * self.r
        self.r *= 0.999

    def find_farthest_point(self):
        distance = self.euclidean(self.x, self.y, self.z, self.points[0][0], self.points[0][1], self.points[0][2])
        index = 0

        for j in range(1, len(self.points)):
            current = self.euclidean(self.x, self.y, self.z, self.points[j][0], self.points[j][1], self.points[j][2])
            if current > distance:
                distance = current
                index = j

        return index, distance

    def solve(self):
        while True:
            n = int(input())
            if n == 0:
                break

            self.points = [tuple(map(float, input().split())) for _ in range(n)]

            self.x, self.y, self.z = map(lambda coord: sum(coord) / n, zip(*self.points))
            self.r = 0.1
            md = 0

            for _ in range(70000):
                index, md = self.find_farthest_point()
                self.update(self.points[index])

            self.x = 0 if round(self.x) == 0 else self.x
            self.y = 0 if round(self.y) == 0 else self.y
            self.z = 0 if round(self.z) == 0 else self.z

            print(f"{md:.5f}")

if __name__ == "__main__":
    sphere_fitting = f()
    sphere_fitting.solve()