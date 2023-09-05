n = int(input())
count = 0

if n < 100:  # 1부터 99까지는 모두 한수이므로 그대로 출력
    print(n)
else:
    count = 99  # 1부터 99까지는 모두 한수이므로 먼저 count를 99로 초기화
    for i in range(100, n + 1):  # 100부터 n까지 한수인지 체크
        nums = list(map(int, str(i)))  # 각 자리 수를 리스트로 저장
        if nums[0] - nums[1] == nums[1] - nums[2]:  # 등차수열인지 확인
            count += 1
    print(count)
