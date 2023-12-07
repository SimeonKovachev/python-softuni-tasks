def add_card(new_deck, original_deck, card_name):
    if card_name in original_deck:
        new_deck.append(card_name)
    else:
        print("Card not found.")


def insert_card(new_deck, original_deck, card_name, index):
    if card_name in original_deck and 0 <= index < len(new_deck):
        new_deck.insert(index, card_name)
    else:
        print("Error!")


def remove_card(new_deck, card_name):
    if card_name in new_deck:
        new_deck.remove(card_name)
    else:
        print("Card not found.")


def swap_cards(new_deck, card_name1, card_name2):
    idx1, idx2 = new_deck.index(card_name1), new_deck.index(card_name2)
    new_deck[idx1], new_deck[idx2] = new_deck[idx2], new_deck[idx1]


def manage_deck():
    original_deck = input().split(":")
    new_deck = []

    while True:
        command = input()
        if command == "Ready":
            break

        parts = command.split()
        action = parts[0]

        if action == "Add":
            add_card(new_deck, original_deck, parts[1])

        elif action == "Insert":
            insert_card(new_deck, original_deck, parts[1], int(parts[2]))

        elif action == "Remove":
            remove_card(new_deck, parts[1])

        elif action == "Swap":
            swap_cards(new_deck, parts[1], parts[2])

        elif command == "Shuffle deck":
            new_deck.reverse()

    print(" ".join(new_deck))


manage_deck()
