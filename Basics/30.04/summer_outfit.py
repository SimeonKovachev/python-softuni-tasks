degrees = int(input())
time_of_the_day = str(input())

outfit = ""
shoes = ""

#ot 10 do 16 gradusa
if 10 <= degrees <= 18 and time_of_the_day == "Morning":
    outfit = "Sweatshirt"
    shoes = "Sneakers"

elif 10 <= degrees <= 18 and time_of_the_day == "Afternoon":
    outfit = "Shirt"
    shoes = "Moccasins"

elif 10 <= degrees <= 18 and time_of_the_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"


# ot  18 do 24 gradusa

elif 18 < degrees <= 24 and time_of_the_day == "Morning":
    outfit = "Shirt"
    shoes = "Moccasins"

elif 18 < degrees <= 24 and time_of_the_day == "Afternoon":
    outfit = "T-Shirt"
    shoes = "Sandals"

elif 18 < degrees <= 24 and time_of_the_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"

#nad 25 gradusa

elif degrees >= 25 and time_of_the_day == "Morning":
    outfit = "T-Shirt"
    shoes = "Sandals"

elif degrees >= 25 and time_of_the_day == "Afternoon":
    outfit = "Swim Suit"
    shoes = "Sandals"

elif degrees >= 25 and time_of_the_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")