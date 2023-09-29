number_of_lines = int(input())
total_sum = 0

for i in range(number_of_lines):
    letter = str(input())

    letter_to_ascii = ord(letter)

    total_sum += letter_to_ascii

print(f"The sum equals: {total_sum}")
