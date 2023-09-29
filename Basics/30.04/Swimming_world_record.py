from math import floor
record_in_seconds = float(input())
razstoqnie_meters = float(input())
seconds_per_meter = float(input())

all_seconds_per_meter = razstoqnie_meters * seconds_per_meter


slow_time = floor(razstoqnie_meters / 15)
all_slow_time = slow_time * 12.5

full_time = all_seconds_per_meter + all_slow_time

if full_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {full_time:.2f} seconds.")

else:
    needed_time = full_time - record_in_seconds
    print(f"No, he failed! He was {needed_time:.2f} seconds slower. ")


