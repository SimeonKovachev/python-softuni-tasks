import re


def find_and_print_eggs(text):
    pattern = re.compile(r'[#@]+(?P<color>[a-z]{3,})([^a-zA-Z\d]*)(\/)+(?P<eggs>\d+)(\/)+')
    matches = pattern.finditer(text)

    for match in matches:
        print(f"You found {match['eggs']} {match['color']} eggs!")


# Example input
input_text = input()
find_and_print_eggs(input_text)
