command = input()

student_ticket_count = 0
standard_ticket_count = 0
kids_ticket_count = 0
total_tickets = 0

while command != "Finish":
    film_name = command
    total_seats = int(input())
    tickets_sold = 0

    type_of_ticket = input()
    while type_of_ticket != "End":
        tickets_sold += 1
        total_tickets += 1
        if type_of_ticket == "student":
            student_ticket_count += 1
        elif type_of_ticket == "standard":
            standard_ticket_count += 1
        elif type_of_ticket == "kid":
            kids_ticket_count += 1
        if tickets_sold >= total_seats:
            break
        type_of_ticket = input()

    cinema_percent = (tickets_sold / total_seats) * 100
    print(f"{film_name} - {cinema_percent:.2f}% full.")

    command = input()

student_tickets_percent = (student_ticket_count / total_tickets) * 100
standard_tickets_percent = (standard_ticket_count / total_tickets) * 100
kids_tickets_percent = (kids_ticket_count / total_tickets) * 100
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_percent:.2f}% student tickets.")
print(f"{standard_tickets_percent:.2f}% standard tickets.")
print(f"{kids_tickets_percent:.2f}% kids tickets.")
