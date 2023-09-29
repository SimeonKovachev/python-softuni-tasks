day_name = str(input())

message = ""
if day_name == "Monday" \
        or day_name == ("Tuesday") \
        or day_name == ("Wednesday") \
        or day_name == ("Thursday") \
        or day_name == ("Friday"):
    message = "Working day"

elif day_name == ("Saturday") \
        or day_name == "Sunday":
    message = "Weekend"

else:
    message = "Error"

print(message)