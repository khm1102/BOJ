def is_han(num):
    # 입력받은 수가 한수인지 검사하는 함수
    if num < 100:
        return True  # 100 미만의 수는 모두 한수이므로 True 반환
    else:
        nums = list(map(int, str(num)))  # 입력받은 수의 각 자리수를 리스트에 저장
        diff = nums[1] - nums[0]  # 두 자리수의 차이를 저장할 변수
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] != diff:  # 두 자리수의 차이가 일정하지 않으면
                return False  # 한수가 아니므로 False 반환
        return True  # 위 조건을 모두 통과하면 한수이므로 True 반환

n = int(input())
cnt = 0  # 한수의 개수를 세는 변수
for i in range(1, n+1):
    if is_han(i):
        cnt += 1
print(cnt)
