sleep_start = int(input())
alarm_time = int(input())
sleep_length = (alarm_time - sleep_start) % 24
print(sleep_length)
