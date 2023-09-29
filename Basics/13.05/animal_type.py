animal_name = str(input())

message = ""
if animal_name == "dog":
    message = "mammal"

elif animal_name == ("crocodile") or animal_name == ("tortoise") or animal_name == ("snake") :
    message = "reptile"

else:
    message = "unknown"

print(message)