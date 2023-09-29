import math

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration * 0.125
rest_duration = break_duration * 0.25
remaining_time = break_duration - lunch_duration - rest_duration

if remaining_time >= episode_duration:
    left_time = remaining_time - episode_duration
    left_time = math.ceil(left_time)
    print(f"You have enough time to watch {series_name} and left with {left_time} minutes free time.")
else:
    needed_time = episode_duration - remaining_time
    needed_time = math.ceil(needed_time)
    print(f"You don't have enough time to watch {series_name}, you need {needed_time} more minutes.")
