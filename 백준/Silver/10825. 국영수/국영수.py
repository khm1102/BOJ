n = int(input())
students = []

def sort_key(student):
    name, korean, english, math = student
    return (-korean, english, -math, name)

for i in range(n):
    name, korean, english, math = input().split()
    students.append((name, int(korean), int(english), int(math)))



students.sort(key=sort_key)

for student in students:
    print(student[0])
    