age = float(input())
gender_word = str(input())

if gender_word == "f":
   if age < 16:
       print("Miss")
   else:
       print("Ms.")

else:
    if age < 16:
        print("Master")
    else:
        print("Mr.")