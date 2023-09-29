girl_pocket_money = float(input())
earned_money_per_day = float(input())
expenses = float(input())
gift_price = float(input())

all_pocket_money = girl_pocket_money * 5
all_earned_money = earned_money_per_day * 5

saved_money = all_pocket_money + all_earned_money
after_expenses = saved_money - expenses

if after_expenses >= gift_price:
    print(f"Profit: {after_expenses:.2f} BGN, the gift has been purchased.")
else:
    needed_money = gift_price - after_expenses
    print(f"Insufficient money: {needed_money:.2f} BGN.")

