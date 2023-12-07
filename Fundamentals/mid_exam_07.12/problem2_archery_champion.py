def process_command(targets, command):
    parts = command.split('@')
    action = parts[0]
    if action == "Shoot Left" or action == "Shoot Right":
        index = int(parts[1])
        length = int(parts[2])
        if 0 <= index < len(targets):
            if action == "Shoot Left":
                target_index = (index - length) % len(targets)
            else:  # Shoot Right
                target_index = (index + length) % len(targets)

            points = min(targets[target_index], 5)
            targets[target_index] -= points
            return points
    return 0


def archery_tournament():
    targets = list(map(int, input().split('|')))
    total_points = 0

    while True:
        command = input()
        if command == "Game over":
            break
        elif command == "Reverse":
            targets.reverse()
        else:
            total_points += process_command(targets, command)

    print(" - ".join(map(str, targets)))
    print(f"John finished the archery tournament with {total_points} points!")


archery_tournament()
