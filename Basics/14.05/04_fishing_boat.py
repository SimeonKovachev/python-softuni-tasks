group_budget = float(input())
season_type = str(input())
fisherman_count = int(input())
rent_price = 0
discount = 0

if season_type == "Spring":
    rent_price = 3000
    if fisherman_count <= 6:
        discount = 0.10
    elif 7 <= fisherman_count <= 11:
        discount = 0.15
    elif fisherman_count >= 12:
        discount = 0.25

elif season_type == "Summer":
    rent_price = 4200
    if fisherman_count <= 6:
        discount = 0.10
    elif 7 <= fisherman_count <= 11:
        discount = 0.15
    elif fisherman_count >= 12:
        discount = 0.25

elif season_type == "Autumn":
    rent_price = 4200
    if fisherman_count <= 6:
        discount = 0.10
    elif 7 <= fisherman_count <= 11:
        discount = 0.15
    elif fisherman_count >= 12:
        discount = 0.25

elif season_type == "Winter":
    rent_price = 2600
    if fisherman_count <= 6:
        discount = 0.10
    elif 7 <= fisherman_count <= 11:
        discount = 0.15
    elif fisherman_count >= 12:
        discount = 0.25

final_price = rent_price - (rent_price * discount)

if season_type != "Autumn":
    if fisherman_count % 2 == 0:
        discount = 0.05
        final_price = final_price - (final_price * discount)

if group_budget >= final_price:
    print(f"Yes! You have {group_budget - final_price:.2f} leva left.")

else:
    print(f"Not enough money! You need {final_price - group_budget:.2f} leva.")
