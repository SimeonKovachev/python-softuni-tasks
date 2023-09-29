arhitecture_name = str(input())
projects_number = int(input())
hours_needed = projects_number * 3
if projects_number >= 0 and projects_number <= 100:
    print(f"The architect {arhitecture_name} will need {hours_needed} hours to complete {projects_number} project/s.")
else:
    print()