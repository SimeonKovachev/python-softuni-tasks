num_count = int(input())

for i in range(num_count):
    num = int(input())

    if num % 2 == 1:
        print(f"{num} is odd!")
        break

else:
    print("All numbers are even.")
