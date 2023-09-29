days_to_stay = int(input())
type_of_room = str(input())
grade = str(input())

nights = days_to_stay - 1
night_price = 0
discount = 1

if days_to_stay < 10:
    if type_of_room == "room for one person":
        night_price = 18.00
    elif type_of_room == "apartment":
        night_price = 25.00
        discount = 0.70
    elif type_of_room == "president apartment":
        night_price = 35.00
        discount = 0.90

elif 10 <= days_to_stay <= 15:
    if type_of_room == "room for one person":
        night_price = 18.00
    elif type_of_room == "apartment":
        night_price = 25.00
        discount = 0.65
    elif type_of_room == "president apartment":
        night_price = 35.00
        discount = 0.85

elif days_to_stay > 15:
    if type_of_room == "room for one person":
        night_price = 18.00
    elif type_of_room == "apartment":
        night_price = 25.00
        discount = 0.50
    elif type_of_room == "president apartment":
        night_price = 35.00
        discount = 0.80

all_nights_price = nights * night_price
final_price = all_nights_price * discount

if grade == "positive":
    final_price += final_price * 0.25

elif grade == "negative":
    final_price -= final_price * 0.10
print(f"{final_price:.2f}")



