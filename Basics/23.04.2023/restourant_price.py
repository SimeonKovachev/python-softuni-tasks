#Пилешко меню –  10.35 лв.
#Меню с риба – 12.40 лв.
#Вегетарианско меню  – 8.15 лв.
#desert  = all sum * 0.20
#dostavka 2.50
num_chicken = int(input()) * 10.35
num_fish= int(input()) * 12.40
num_vegan = int(input()) * 8.15
all_sum = num_chicken + num_fish + num_vegan
desert = all_sum * 0.20
shipping = 2.50
final_price = all_sum + desert + shipping
print(final_price)

