exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_time = exam_hour * 60 + exam_min
arrival_time = arrival_hour * 60 + arrival_min
time_diff = arrival_time - exam_time

if time_diff > 0:
    print("Late")
elif time_diff >= -30:
    print("On time")
else:
    print("Early")

if time_diff != 0:
    hours = abs(time_diff) // 60
    minutes = abs(time_diff) % 60
    if hours == 0:
        print(f"{minutes} minutes {'after' if time_diff > 0 else 'before'} the start")
    else:
        print(f"{hours}:{minutes:02d} hours {'after' if time_diff > 0 else 'before'} the start")