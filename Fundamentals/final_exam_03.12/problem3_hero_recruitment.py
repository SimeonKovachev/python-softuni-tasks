heroes = {}

while True:
    command = input()

    if command == "End":
        break

    command_parts = command.split()
    action = command_parts[0]
    hero_name = command_parts[1]

    if action == "Enroll":
        if hero_name not in heroes:
            heroes[hero_name] = set()
        else:
            print(f"{hero_name} is already enrolled.")
    elif action == "Learn":
        spell_name = command_parts[2]
        if hero_name in heroes:
            if spell_name not in heroes[hero_name]:
                heroes[hero_name].add(spell_name)
            else:
                print(f"{hero_name} has already learnt {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")
    elif action == "Unlearn":
        spell_name = command_parts[2]
        if hero_name in heroes:
            if spell_name in heroes[hero_name]:
                heroes[hero_name].remove(spell_name)
            else:
                print(f"{hero_name} doesn't know {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")

print("Heroes:")
for hero_name, spells in (heroes.items()):
    spells_str = ', '.join(sorted(spells))
    print(f"== {hero_name}: {spells_str}")
