numbers = list(range(1, 10_001))
remove_list = []  
for num in numbers :
    for n in str(num):
        num += int(n)  
    if num <= 10_000:  
        remove_list.append(num)  # append: 리스트에 요소를 추가할 때

for remove_num in set(remove_list) :  # set 으로 중복값 제거
    numbers.remove(remove_num)
for self_num in numbers :  # 생성자가 있는 숫자를 삭제한 리스트
    print(self_num)