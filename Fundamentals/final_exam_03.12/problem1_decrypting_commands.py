def process_commands(message):
    while True:
        command = input()
        if command == "Finish":
            break

        parts = command.split()
        action = parts[0]

        if action == "Replace":
            current_char, new_char = parts[1], parts[2]
            message = message.replace(current_char, new_char)
            print(message)

        elif action == "Cut":
            start_index, end_index = int(parts[1]), int(parts[2])
            if 0 <= start_index <= end_index < len(message):
                message = message[:start_index] + message[end_index + 1:]
                print(message)
            else:
                print("Invalid indices!")

        elif action == "Make":
            case = parts[1]
            if case == "Upper":
                message = message.upper()
            elif case == "Lower":
                message = message.lower()
            print(message)

        elif action == "Check":
            string = parts[1]
            if string in message:
                print(f"Message contains {string}")
            else:
                print(f"Message doesn't contain {string}")

        elif action == "Sum":
            start_index, end_index = int(parts[1]), int(parts[2])
            if 0 <= start_index <= end_index < len(message):
                substring = message[start_index:end_index + 1]
                ascii_sum = sum(ord(char) for char in substring)
                print(ascii_sum)
            else:
                print("Invalid indices!")

# Main execution
input_message = input()
process_commands(input_message)
