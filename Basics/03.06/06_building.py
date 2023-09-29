number_of_floors = int(input())
number_of_rooms = int(input())
floor_letter = ""

for floor in range(number_of_floors, 0, -1):
    if number_of_floors == floor:
        floor_letter = "L"
    elif floor % 2 == 0:
        floor_letter = "O"
    else:
        floor_letter = "A"

    for room in range(number_of_rooms):
        print(f"{floor_letter}{floor}{room}", end=" ")
    print()

