destination = input()
while destination != "End":
    budget = 0
    needed_budget = float(input())

    while budget < needed_budget:
        saved_money = float(input())
        budget += saved_money
    print(f"Going to {destination}!")

    destination = input()

