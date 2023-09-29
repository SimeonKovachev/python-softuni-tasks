hour = int(input())
day_of_week = str(input())

condition = "closed"
if day_of_week == "Monday" \
        or day_of_week == "Tuesday" \
        or day_of_week == "Wednesday" \
        or day_of_week == "Thursday" \
        or day_of_week == "Friday" \
        or day_of_week == "Saturday":
    if 10 <= hour <= 18:
       condition = "open"

print(condition)

