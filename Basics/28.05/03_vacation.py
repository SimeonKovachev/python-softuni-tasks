money_needed_for_trip = float(input())
current_money = float(input())

spend_days = 0
all_days = 0

while current_money <= money_needed_for_trip:
    type_of_action = input()
    sum_for_action = float(input())

    if type_of_action == "spend":
        spend_days += 1
        all_days += 1
        if spend_days == 5:
            print("You can't save the money.")
            print(f"{all_days}")
            break
        current_money -= sum_for_action
        if current_money < 0:
            current_money = 0

    elif type_of_action == "save":
        current_money += sum_for_action
        spend_days = 0
        all_days += 1

        if current_money >= money_needed_for_trip:
            print(f"You saved the money for {all_days} days.")
            break


