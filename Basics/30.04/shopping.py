budget = float(input())
video_count = int(input())
cpu_count = int(input())
ram_count = int(input())

#cenite
video_price = 250 * video_count
cpu_price = (0.35 * video_price) * cpu_count
ram_price = (0.10 * video_price) * ram_count

all_price = video_price + cpu_price + ram_price
if video_count > cpu_count:
    all_price = all_price - (all_price * 0.15)

if budget >= all_price:
    left_price = all_price - budget
    print(f"You have {abs(left_price):.2f} leva left!")

else:
    needed_price = budget - all_price
    print(f"Not enough money! You need {abs(needed_price):.2f} leva more!")

