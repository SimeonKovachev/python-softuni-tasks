judge_count = int(input())
command = input()
overall_grade = 0
all_judges = 0

while command != "Finish":
    presentation_grade = 0

    for i in range(judge_count):
        judge_grade = float(input())
        presentation_grade += judge_grade
        overall_grade += judge_grade
        all_judges += 1
    print(f"{command} - {presentation_grade / judge_count:.2f}.")
    command = input()

print(f"Student's final assessment is {overall_grade/ all_judges:.2f}.")

