age = int(input())
washer_price = float(input())
toy_price = int(input())

toy_count = 0
savings = 0

for birthday in range (1, age + 1):

    if birthday % 2 == 0:
        savings += birthday * 5
        savings -= 1
    else:
        toy_count += 1


savings += toy_price * toy_count

if savings >= washer_price:
    diff = savings - washer_price
    print(f"Yes! {diff:.2f}")

else:
    diff = washer_price - savings
    print(f"No! {diff:.2f}")
