ROSES_PRICE =  5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

flower_type = str(input())
number_flowers = int(input())
budget = float(input())

price = 0
discount = 0

if flower_type == "Roses":
    price = ROSES_PRICE
    if number_flowers > 80 :
        discount = 0.10

elif flower_type == "Dahlias":
    price = DAHLIAS_PRICE
    if number_flowers > 90 :
        discount = 0.15

elif flower_type == "Tulips":
    price = TULIPS_PRICE
    if number_flowers > 80 :
        discount = 0.15

elif flower_type == "Narcissus":
    price = NARCISSUS_PRICE
    if number_flowers < 120 :
        discount = -0.15

elif flower_type == "Gladiolus":
    price = GLADIOLUS_PRICE
    if number_flowers < 80 :
        discount = -0.20

total_price = (number_flowers * price) * (1-discount)


if budget >= total_price:
    print(f"Hey, you have a great garden with {number_flowers} {flower_type} and {budget-total_price :.2f} leva left.")

else:
    print(f"Not enough money, you need {total_price - budget :.2f} leva more.")