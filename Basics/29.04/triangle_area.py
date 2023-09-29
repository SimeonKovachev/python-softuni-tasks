from math import pi

type_of_the_figure = str(input())

# Vinagi predefinirame promenlivite koito imame, za da nqmame greshka nakraq pri print nakraq.
area = 0

if type_of_the_figure == "square":
    width = float(input())
    area = width * width
elif type_of_the_figure == "rectangle":
    width_a = float(input())
    width_b = float(input())
    area = width_a * width_b
elif type_of_the_figure == "circle":
    radius = float(input())
    area = pi * (radius ** 2)
elif type_of_the_figure == "triangle":
    width = float(input())
    height = float(input())
    area = width * height / 2

print(f"{area:.3f}")
