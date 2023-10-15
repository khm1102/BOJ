import sys
def input(): return sys.stdin.readline().strip()
def print(val):return sys.stdout.write(str(val))
class Stock:
    def __init__(self, money, share):
        self.m = money
        self.s = share

    def buy(self, cost, count):
        if self.m < cost * count:
            return
        self.s += count
        self.m -= cost * count

    def sell(self, cost):
        self.m += cost * self.s
        self.s = 0

def B(n, w):
    stock = Stock(n, 0)
    for i in range(14):
        cash = stock.m
        share = cash // w[i]
        if share > 0:
            stock.buy(w[i], share)

    return stock.m + (stock.s * w[13])


def T(n, w):
    stock = Stock(n, 0)
    for i in range(3, 14):
        cash = stock.m
        share = cash // w[i]
        if w[i - 1] > w[i - 2] and w[i - 2] > w[i - 3]:
            stock.sell(w[i])
        if w[i - 1] < w[i - 2] and w[i - 2] < w[i - 3]:
            stock.buy(w[i], share)

    return stock.m + (stock.s * w[13])


n = int(input())
week = list(map(int, input().split()))

junhyun = B(n, week)
sungmin = T(n, week)

print("BNP" if junhyun > sungmin else "TIMING" if junhyun < sungmin else "SAMESAME")