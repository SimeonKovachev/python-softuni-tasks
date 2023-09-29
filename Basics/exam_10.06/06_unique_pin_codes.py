first_number = int(input())
second_number = int(input())
third_number = int(input())

for n1 in range(2, first_number + 1, 2):
    for n2 in range(2, second_number + 1):
        if n2 == 2 or n2 == 3 or n2 == 5 or n2 == 7:
            for n3 in range(2, third_number + 1, 2):
                print(f"{n1} {n2} {n3}")
