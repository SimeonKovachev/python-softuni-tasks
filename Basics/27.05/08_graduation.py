# student_name = input()
# class_number = 1
# grade_sum = 0
# excluded_count = 0
#
# while class_number <= 12:
#     grade_number = float(input())
#     if grade_number < 4.00:
#         excluded_count += 1
#         if excluded_count > 1:
#             break
#         continue
#     class_number += 1
#     grade_sum += grade_number
#
# if class_number <= 12:
#     print(f"{student_name} has been excluded at {class_number} grade")
#
# else:
#     print(f"{student_name} graduated. Average grade: {grade_sum / 12:.2f}")





#Vtori nachin s print napravo v purviq if

# student_name = input()
# class_number = 1
# grade_sum = 0
# excluded_count = 0
#
# while class_number <= 12:
#     grade_number = float(input())
#     if grade_number < 4.00:
#         excluded_count += 1
#         if excluded_count > 1:
#             print(f"{student_name} has been excluded at {class_number} grade")
#             break
#         continue
#     class_number += 1
#     grade_sum += grade_number
#
# else:
#     print(f"{student_name} graduated. Average grade: {grade_sum / 12:.2f}")




#Treti nachin s boolean promenliva

student_name = input()
class_number = 1
grade_sum = 0
excluded_count = 0
is_excluded = False

while class_number <= 12:
    grade_number = float(input())
    if grade_number < 4.00:
        excluded_count += 1
        if excluded_count > 1:
            is_excluded = True
            break
        continue
    class_number += 1
    grade_sum += grade_number

if is_excluded:
    print(f"{student_name} has been excluded at {class_number} grade")

else:
    print(f"{student_name} graduated. Average grade: {grade_sum / 12:.2f}")
