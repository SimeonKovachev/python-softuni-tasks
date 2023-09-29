import math
from math import  floor
list_num = int(input())
list_per_hour = int(input())
days = int(input())
full_time = list_num / list_per_hour
time_per_day = full_time / days
print(math.floor(time_per_day))