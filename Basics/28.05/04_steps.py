steps = 0
wanted_steps = 10000

command = input()

while command != "Going home":
    current_steps = int(command)
    steps += current_steps

    if steps >= wanted_steps:
        break
    command = input()

if command == "Going home":
    current_steps = int(input())
    steps += current_steps

if steps >= wanted_steps:
    step_difference = steps - wanted_steps
    print(f"Goal reached! Good job!")
    print(f"{step_difference} steps over the goal!")

else:
    step_difference = wanted_steps - steps
    print(f"{step_difference} more steps to reach goal.")




