def solution(heights):
    heights.sort()
    arr = []
    if len(heights) % 2 == 1:
        for i in range(len(heights) // 2):
            arr.append(heights[i + len(heights) // 2] - heights[i])
        arr.append(heights[-1] - heights[len(heights) // 2])
        arr.sort()
        return arr[1]
    else:
        for i in range(len(heights) // 2):
            arr.append(heights[i + len(heights) // 2] - heights[i])
        arr.sort()
        return arr[0]