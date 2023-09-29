command = str(input())
coffee_points = 0

while command != "END":
    if command.lower() == "coding" \
           or command.lower() == "cat" \
           or command.lower() == "dog"\
           or command.lower() == "movie":
        if command.islower():
            coffee_points += 1
        else:
            coffee_points += 2

    command = str(input())

if coffee_points > 5:
    print("You need extra sleep")

else:
    print(coffee_points)
