number = int(input())

for i in range(1, number + 1):
    sum_of_digits = 0
    current_number_as_string = str(i)

    for digit in current_number_as_string:
        sum_of_digits += int(digit)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{i} -> True")

    else:
        print(f"{i} -> False")
