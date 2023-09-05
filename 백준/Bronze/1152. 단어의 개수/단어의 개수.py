s = input().strip()  # 문자열 입력받기 (양쪽 공백 제거)
words = s.split()  # 문자열을 공백을 기준으로 분리하여 리스트로 만들기
count = len(words)  # 분리된 문자열의 개수 세기

print(count)  # 단어의 개수 출력
