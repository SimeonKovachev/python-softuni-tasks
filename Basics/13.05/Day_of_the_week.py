week_number = int(input())

message = ""
if week_number == 1:
    message = "Monday"

elif week_number == 2:
    message = ("Tuesday")

elif week_number == 3:
    message = ("Wednesday")

elif week_number == 4:
    message = ("Thursday")

elif week_number == 5:
    message = ("Friday")

elif week_number == 6:
    message = ("Saturday")

elif week_number == 7:
    message = ("Sunday")

else:
    message = ("Error")

print(message)