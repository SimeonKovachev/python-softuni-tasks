product_name = str(input())
type_of_product = "unknown"

if product_name == "banana" \
        or product_name == "apple" \
        or product_name == "kiwi" \
        or product_name == "cherry" \
        or product_name == "lemon" \
        or product_name == "grapes":
    type_of_product = "fruit"

elif product_name == "tomato" \
        or product_name == "cucumber" \
        or product_name == "pepper" \
        or product_name == "carrot":
    type_of_product = "vegetable"

print(type_of_product)
