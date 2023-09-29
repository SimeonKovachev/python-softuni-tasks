kil_per_meter = float(input())
price_per_meter = kil_per_meter * 7.61
discount = price_per_meter * 0.18
final_price = price_per_meter - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")