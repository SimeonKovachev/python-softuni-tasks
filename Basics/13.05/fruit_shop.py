product_name = str(input())
day_of_week = str(input())
quantity = float(input())
price = 0

#Working days
if day_of_week == "Monday" \
        or day_of_week == "Tuesday" \
        or day_of_week == "Wednesday" \
        or day_of_week == "Thursday" \
        or day_of_week == "Friday":
    if product_name == "banana":
        price = 2.50
    elif product_name == "apple":
        price = 1.20
    elif product_name == "orange":
        price = 0.85
    elif product_name == "grapefruit":
        price = 1.45
    elif product_name == "kiwi":
        price = 2.70
    elif product_name == "pineapple":
        price = 5.50
    elif product_name == "grapes":
        price = 3.85

#Weekend
elif day_of_week == "Saturday" \
        or day_of_week == "Sunday":
    if product_name == "banana":
        price = 2.70
    elif product_name == "apple":
        price = 1.25
    elif product_name == "orange":
        price = 0.90
    elif product_name == "grapefruit":
        price = 1.60
    elif product_name == "kiwi":
        price = 3.00
    elif product_name == "pineapple":
        price = 5.60
    elif product_name == "grapes":
        price = 4.20

if price == 0:
    print("error")

else:
    final_price = quantity * price
    print(f"{final_price:.2f}")


