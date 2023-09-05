import math

def main():
    input_data = input().split()
    x = float(input_data[0])
    y = float(input_data[1])
    c = float(input_data[2])

    left = 0
    right = min(x, y)

    while right - left >= 0.001:
        width = (left + right) / 2
        h1 = math.sqrt(x**2 - width**2)
        h2 = math.sqrt(y**2 - width**2)
        res = (h1 * h2) / (h1 + h2)

        if res >= c:
            left = width
        else:
            right = width
    
    print("{:.3f}".format(right))

if __name__ == "__main__":
    main()
