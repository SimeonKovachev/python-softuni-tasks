num_lines = int(input())

for i in range(num_lines):
    num_of_message = int(input())

    if num_of_message == 88:
        print("Hello")

    elif num_of_message == 86:
        print("How are you?")

    elif num_of_message > 88:
        print("Bye.")

    else:
        print("GREAT!")
