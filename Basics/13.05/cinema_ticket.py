day_name = str(input())
cinema_ticket = 0

if day_name == "Monday" \
        or day_name == "Tuesday" \
        or day_name == ("Friday"):
    cinema_ticket = 12

elif day_name == "Wednesday" \
        or day_name == "Thursday":
    cinema_ticket = 14

elif day_name == "Saturday" \
        or day_name == "Sunday":
    cinema_ticket = 16

print(cinema_ticket)