pen_packet = float(input()) * 5.8
marker_packet = float(input()) * 7.2
spray_litres = float(input()) * 1.2
percentage = float(input()) / 100
all_price = (pen_packet + marker_packet + spray_litres)
fianl_sum = all_price - all_price * percentage
print(fianl_sum)
