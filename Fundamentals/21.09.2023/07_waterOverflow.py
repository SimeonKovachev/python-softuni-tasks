number_of_lines = int(input())

tank_capacity = 255
current_capacity = 0

for i in range(number_of_lines):
    liters_of_water = int(input())

    if tank_capacity >= current_capacity:
        current_capacity += liters_of_water

    else:
        print("Insufficient capacity!")
        continue

print(current_capacity)


