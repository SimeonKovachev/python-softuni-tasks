cinema_type = str(input())
row = int(input())
col = int(input())
price = 0
cinema_space = row * col

if cinema_type == "Premiere":
    price = 12.00

elif cinema_type == "Normal":
    price = 7.50

elif cinema_type == "Discount":
    price = 5.00

final_price = cinema_space * price
print(f"{final_price:.2f} leva")
