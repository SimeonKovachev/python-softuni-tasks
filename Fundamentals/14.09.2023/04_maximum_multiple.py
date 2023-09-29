divisor_num = int(input())
boundary_num = int(input())

for current_num in range(boundary_num, divisor_num - 1, -1):

    if current_num % divisor_num == 0 and boundary_num >= current_num > 0:

        print(current_num)
        break
