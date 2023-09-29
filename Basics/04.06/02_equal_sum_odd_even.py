num1 = int(input())
num2 = int(input())

for current_number in range(num1, num2+1):
    a_odd = 0
    b_even = 0
    number_to_str = str(current_number)

    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            a_odd += int(digit)
        else:
            b_even += int(digit)

    if a_odd == b_even:
        print(number_to_str, end=" ")
