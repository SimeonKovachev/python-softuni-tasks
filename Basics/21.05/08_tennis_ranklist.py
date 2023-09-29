
tornament_number = int(input())
starter_points = int(input())

winned_tournaments = 0
total_points = starter_points

for i in range(tornament_number):
    tornament_stage = input()
    if tornament_stage == "W":
        winned_tournaments += 1
        total_points += 2000
    elif tornament_stage == "F":
        total_points += 1200
    elif tornament_stage == "SF":
        total_points += 720

avarage_points = (total_points - starter_points) // tornament_number
winned_per = (winned_tournaments / tornament_number) * 100

print(f"Final points: {total_points}")
print(f"Average points: {avarage_points}")
print(f"{winned_per:.2f}%")
