start_ascii_point = int(input())
end_ascii_point = int(input())

for char in range(start_ascii_point, end_ascii_point + 1):
    print(chr(char), end=' ')
