# import sys
#
# num_of_numbers = int(input())
# # pomoshni promenlivi s mnogo visoki stoinosti za da moje posle da sravnqvame koe e po golqmo i po malko
# # pri max_number = -sys.maxsize e s minus zashtoto se sravnqva dali nai malkoto chislo e po golqmo or tekushtoto
# max_number = -sys.maxsize
# min_number = sys.maxsize
# for i in range(num_of_numbers):
#     number = int(input())
#     if number > max_number:
#         max_number = number
#     if number < min_number:
#         min_number = number
#
# print(f"Max number: {max_number}")
# print(f"Min number: {min_number}")



# drugoto reshenie zadavame purvoto vuvedeno chislo kato max i min number i posle sravnqvame s tqh
num_of_numbers = int(input())
number = int(input())
min_number = number
max_number = number

for i in range(num_of_numbers - 1):
    number = int(input())
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")

