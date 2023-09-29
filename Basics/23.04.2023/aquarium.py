# paralepiped
# input width, height , length
length = int(input())
width = int(input())
height = int(input())
percentage = float(input())
volume = length * width * height
liters = volume * 0.001
occupied_space = percentage / 100
all_liters = liters * (1 - occupied_space)
print(all_liters)