trip_price = float(input())
puzzle_number = int(input())
speaking_doll_number = int(input())
teddy_bear_number = int(input())
minion_number = int(input())
truck_number = int(input())

win_price = 0
left_price = 0
final_price = 0

#ceni na igrachkite
puzzle = 2.60 * puzzle_number
speaking_doll = 3 * speaking_doll_number
teddy_bear = 4.10 * teddy_bear_number
minion = 8.20 * minion_number
truck = 2 * truck_number

product_price = puzzle + speaking_doll + teddy_bear + minion +  truck

product_number = puzzle_number + speaking_doll_number + teddy_bear_number + minion_number + truck_number

if product_number >= 50:
    with_percentage_price = product_price * 0.25
    final_price = product_price - with_percentage_price
    rent = final_price * 0.10
    win_price = final_price - rent
    left_price = win_price - trip_price
    print(f"Yes! {left_price:.2f} lv left.")

else:
    rent = product_price * 0.10
    win_price = product_price - rent
    not_enough_price = trip_price - win_price
    print(f"Not enough money! {not_enough_price:.2f} lv needed.")
