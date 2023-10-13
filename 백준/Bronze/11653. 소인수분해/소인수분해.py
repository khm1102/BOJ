n = int(input()) 

if n == 1:
    pass  
else:
    i = 2  
    while n != 1:
        if n % i == 0:  # i가 N의 약수인 경우
            print(i)  
            n //= i  # N을 i로 나누어 갱신
        else:  
            i += 1  # 다음 소수를 시도
