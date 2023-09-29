n = int(input())

for number in range(1111, 10000):
    current_number = number
    is_special = True

    while current_number > 0:
        digit = current_number % 10

        if digit == 0 or n % digit != 0:
            is_special = False
            break

        current_number //= 10

    if is_special:
        print(number, end=" ")


