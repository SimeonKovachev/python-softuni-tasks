from math import floor

timefirst = int(input())
timesecond = int(input())
timethird = int(input())

total_time = timefirst + timesecond + timethird

minutes = total_time // 60
seconds = total_time % 60

minutes = floor(minutes)

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
