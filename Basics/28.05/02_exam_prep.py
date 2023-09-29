acceptable_grades = int(input())

tasks_count = 0
grade_sum = 0
excluded_count = 0
last_task = ""

while excluded_count < acceptable_grades:
    problem_name = input()
    if problem_name == "Enough":
        average_grade = grade_sum / tasks_count
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {tasks_count}")
        print(f"Last problem: {last_task}")
        break
    grade = float(input())
    if grade <= 4.00:
        excluded_count += 1

    tasks_count += 1
    grade_sum += grade
    last_task = problem_name
else:
    print(f"You need a break, {excluded_count} poor grades.")


