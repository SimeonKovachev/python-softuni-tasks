days_to_stay = int(input())
budget = float(input())
passengers = int(input())
fuel_price_km = float(input())
food_expense = float(input())  # per person for a day
room_price = float(input())  # price for a night per person (nights = days - 1)

total_food_expense = food_expense * days_to_stay * passengers
total_room_expense = room_price * days_to_stay * passengers

# Discount on accommodation if the group is larger than 10
if passengers > 10:
    total_room_expense -= total_room_expense * 0.25

total_expense = total_food_expense + total_room_expense

# Calculating daily expenses
for day in range(1, days_to_stay + 1):
    traveled_distance = float(input())
    daily_fuel_expense = traveled_distance * fuel_price_km
    total_expense += daily_fuel_expense

    # Additional expenses every 3rd and 5th day
    if day % 3 == 0 or day % 5 == 0:
        total_expense += total_expense * 0.40

    # Receiving money every 7th day
    if day % 7 == 0:
        total_expense -= total_expense / passengers

    # Check if budget is exceeded
    if total_expense > budget:
        money_needed = total_expense - budget
        print(f"Not enough money to continue the trip. You need {money_needed:.2f}$ more.")
        break
else:  # This 'else' executes if the loop wasn't 'break'ed, meaning they have enough money
    money_left = budget - total_expense
    print(f"You have reached the destination. You have {money_left:.2f}$ budget left.")




