from sys import maxsize

numbers_count = int(input())

max_num = -maxsize
sum_num = 0
for numbers in range (numbers_count):
    current_number = int(input())

    if current_number > max_num:
        max_num = current_number

    sum_num += current_number

rest_sum = sum_num - max_num
if max_num == rest_sum:
    print(f"Yes\nSum = {sum_num - max_num}")

else:
    diff  = abs(rest_sum - max_num)
    print(f"No\nDiff = {diff}")