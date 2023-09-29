free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

free_space_area = free_space_length * free_space_width * free_space_height
while free_space_area > 0:
    command = input()

    if command == "Done":
        print(f"{free_space_area} Cubic meters left.")
        break
    number_boxes = int(command)
    free_space_area -= number_boxes

else:
    difference = abs(free_space_area)
    print(f"No more free space! You need {difference} Cubic meters more.")
