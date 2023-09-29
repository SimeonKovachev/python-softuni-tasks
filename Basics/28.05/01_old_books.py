searched_book = input()
command = input()
books_checked = 0

while command != "No More Books":
    command = input()
    books_checked += 1

    if searched_book == command:
        print(f"You checked {books_checked} books and found it.")
        break

else:
    print("The book you search is not here!")
    print(f"You checked {books_checked} books.")







