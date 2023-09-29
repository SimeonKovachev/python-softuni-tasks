text = input()
points = 0

for char in range(0, len(text)):
    current_letter = text[char]
    if current_letter == "a":
        points += 1
    elif current_letter == "e":
        points += 2
    elif current_letter == "i":
        points += 3
    elif current_letter == "o":
        points += 4
    elif current_letter == "u":
        points += 5

print(points)