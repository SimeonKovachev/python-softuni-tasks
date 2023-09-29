actor_name = input()
academy_points = float(input())
number_of_graders = int(input())

required_points = 1250.5

for i in range (number_of_graders):
    grader_name = input()
    grader_points = float(input())

    academy_points += (len(grader_name) * grader_points) / 2

    if academy_points > required_points:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break

else:
    print(f"Sorry, {actor_name} you need {required_points - academy_points:.1f} more!")
