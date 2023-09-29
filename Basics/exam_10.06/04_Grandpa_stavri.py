days_number = int(input())
liters = 0
degree = 0

for days in range(days_number):
    rakia_quantity = float(input())
    rakia_degree = float(input())

    liters += rakia_quantity
    degree += rakia_degree * rakia_quantity

average_degree = degree / liters

print(f"Liter: {liters:.2f}")
print(f"Degrees: {average_degree:.2f}")
if average_degree < 38:
    print("Not good, you should baking!")
elif average_degree <= 42:
    print("Super!")
elif average_degree > 42:
    print("Dilution with distilled water!")


