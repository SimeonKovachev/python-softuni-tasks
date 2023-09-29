current_meters = 5364
everest = 8848
days_count = 1

while True:
    command = input()

    if command == "END":
        break

    sleep_condition = command
    meters_climbed = int(input())

    current_meters += meters_climbed

    if sleep_condition == "Yes":
        days_count += 1

    if current_meters >= everest or days_count > 5:
        break

if current_meters >= everest:
    print(f"Goal reached for {days_count} days!")
elif days_count > 5:
    current_meters -= meters_climbed
    print("Failed!")
    print(current_meters)
else:
    print("Failed!")
    print(current_meters)
