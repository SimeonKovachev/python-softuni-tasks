film_budget = float(input())
statists_count = int(input())
statis_price = float(input())

decor_forfilm = 0.10 * film_budget
total_price_forstatists = statists_count * statis_price
#pri poveche ot 150 statista ima ostupka ot 10% ot oblekloto
if statists_count > 150:
    total_price_forstatists = total_price_forstatists - (total_price_forstatists * 0.10)

all_priceforthefilm = decor_forfilm + total_price_forstatists

price_left = film_budget - all_priceforthefilm

if all_priceforthefilm > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(price_left):.2f} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {abs(price_left):.2f} leva left.")

