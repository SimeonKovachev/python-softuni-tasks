city_name = str(input())
quantity = float(input())
percentage = 0

if city_name == "Sofia":
    if  0 <= quantity <= 500:
        percentage = 0.05
    elif 501 <= quantity <= 1000:
        percentage = 0.07
    elif 1001 <= quantity <= 10000:
        percentage = 0.08
    elif quantity > 10000:
        percentage = 0.12

elif city_name == "Plovdiv":
    if 0 <= quantity <= 500:
        percentage = 0.055
    elif 501 <= quantity <= 1000:
        percentage = 0.08
    elif 1001 <= quantity <= 10000:
        percentage = 0.12
    elif quantity > 10000:
        percentage = 0.145

elif city_name == "Varna":
    if 0 <= quantity <= 500:
        percentage = 0.045
    elif 501 <= quantity <= 1000:
        percentage = 0.075
    elif 1001 <= quantity <= 10000:
        percentage = 0.10
    elif quantity > 10000:
        percentage = 0.13

if percentage == 0:
    print("error")

else:
    final_price = quantity * percentage
    print(f"{final_price:.2f}")