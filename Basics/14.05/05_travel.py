budget = float(input())
season = str(input())

journey_type = ""
journey_destination = ""
spent_money = 0

if budget <= 100:
    journey_destination = "Bulgaria"
    if season == "summer":
        journey_type ="Camp"
        spent_money = 0.30
    elif season == "winter":
        journey_type = "Hotel"
        spent_money = 0.70

elif budget <= 1000:
    journey_destination = "Balkans"
    if season == "summer":
        journey_type = "Camp"
        spent_money = 0.40
    elif season == "winter":
        journey_type = "Hotel"
        spent_money = 0.80

elif budget > 1000:
    journey_destination = "Europe"
    if season == "summer" or season == "winter":
        journey_type = "Hotel"
        spent_money = 0.90

final_price = budget * spent_money

print(f"Somewhere in {journey_destination}")
print(f"{journey_type} - {final_price:.2f}")