people_number = int(input())
nights_number = int(input())
cards_per_night = int(input())
museum_ticket_number = int(input())

night_price = 20 * nights_number
transport_card = 1.60 * cards_per_night
museum_ticket = 6 * museum_ticket_number

cost_per_person = night_price + transport_card + museum_ticket
all_people_price = cost_per_person * people_number

final_price = all_people_price + (all_people_price * 0.25)

print(f"{final_price:.2f}")
