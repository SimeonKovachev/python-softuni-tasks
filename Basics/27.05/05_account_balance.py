total_sum = 0
command = input()

while command != "NoMoreMoney":
    current_sum = float(command)
    if current_sum < 0:
        print(f"Invalid operation!")
        break
        #continue ni vrushta otgore v nachaloto na while cikula, no trqbva da ima nqkakva stoinost koqto da se
        #priema inache ostava v bezkraen cikul!!!
        # command = input()
        # continue

    print(f"Increase: {current_sum:.2f}")
    total_sum += current_sum
    command = input()

print(f"Total: {total_sum:.2f}")
