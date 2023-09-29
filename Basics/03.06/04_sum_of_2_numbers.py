start_number = int(input())
end_number = int(input())
magic_number = int(input())

is_found = False

combination_count = 0

for num1 in range(start_number, end_number + 1):
    for num2 in range(start_number, end_number + 1):
        combination_count += 1
        if num1 + num2 == magic_number:
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f"Combination N:{combination_count} ({num1} + {num2} = {magic_number})")

else:
    print(f"{combination_count} combinations - neither equals {magic_number}")





