width = int(input())
length = int(input())

cake_area = width * length

while cake_area > 0:
    command = input()
    if command == "STOP":
        print(f"{cake_area} pieces are left.")
        break
    cake_taken = int(command)
    cake_area -= cake_taken

else:
    difference = abs(cake_area)
    print(f"No more cake left! You need {difference} pieces more.")
