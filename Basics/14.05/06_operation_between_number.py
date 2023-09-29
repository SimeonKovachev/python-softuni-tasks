number1 = int(input())
number2 = int(input())
operator = input()
total = 0
even_or_odd = ""

if operator == "+":
    total = number1 + number2
    if total % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{number1} {operator} {number2} = {total} - {even_or_odd}")
elif operator == "-":
    total = number1 - number2
    if total % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{number1} {operator} {number2} = {total} - {even_or_odd}")
elif operator == "*":
    total = number1 * number2
    if total % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{number1} {operator} {number2} = {total} - {even_or_odd}")
elif operator == "/":
    if number2 != 0:
        total = number1 / number2
        print(f"{number1} {operator} {number2} = {total:.2f}")
    else:
        print(f"Cannot divide {number1} by zero")
elif operator == "%":
    if number2 != 0:
        total = number1 % number2
        print(f"{number1} {operator} {number2} = {total}")
    else:
        print(f"Cannot divide {number1} by zero")



n1 = int(input())
n2 = int(input())
operator = input()

# check for valid operator and calculate result accordingly
if operator == "+":
    result = n1 + n2
    print(f"{n1} {operator} {n2} = {result} - {'even' if result % 2 == 0 else 'odd'}")
elif operator == "-":
    result = n1 - n2
    print(f"{n1} {operator} {n2} = {result} - {'even' if result % 2 == 0 else 'odd'}")
elif operator == "*":
    result = n1 * n2
    print(f"{n1} {operator} {n2} = {result} - {'even' if result % 2 == 0 else 'odd'}")
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")
else:
    print("Invalid operator")