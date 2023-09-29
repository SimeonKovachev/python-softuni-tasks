num_of_orders = int(input())
total_price = 0

for i in range(num_of_orders):
    price_per_capsule = float(input())
    if not 0.01 <= price_per_capsule <= 100:
        continue
    days = int(input())
    if not 1 <= days <= 31:
        continue
    capsules_per_day = int(input())
    if not 1 <= capsules_per_day <= 2000:
        continue

    price = (capsules_per_day * days) * price_per_capsule
    total_price += price

    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")
