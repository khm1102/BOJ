import calendar

x, y = map(int, input().split())
weekday = calendar.weekday(2007, x, y)
print(calendar.day_name[weekday][:3].upper())