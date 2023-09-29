max_row = int(input())

for i in range(1, max_row + 1):
    for j in range(0, i):
        print('*', end='')
    print()

for i in range(max_row - 1, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()
