climbers_number = int(input())
musala = monblan = kilimandjaro = k2 = everest = 0

for i in range (climbers_number):
    people_in_group = int(input())

    if people_in_group <= 5:
        musala += people_in_group
    elif people_in_group <= 12:
        monblan += people_in_group
    elif people_in_group <= 25:
        kilimandjaro += people_in_group
    elif people_in_group <= 40:
        k2 += people_in_group
    else:
        everest += people_in_group

all_climbers = musala + monblan + kilimandjaro + k2 + everest

musala_per = musala / all_climbers * 100
monblan_per = monblan / all_climbers * 100
kilimandjaro_per = kilimandjaro / all_climbers * 100
k2_per = k2 / all_climbers * 100
everest_per = everest / all_climbers * 100

print(f"{musala_per:.2f}%\n"
      f"{monblan_per:.2f}%\n"
      f"{kilimandjaro_per:.2f}%\n"
      f"{k2_per:.2f}%\n"
      f"{everest_per:.2f}%\n")