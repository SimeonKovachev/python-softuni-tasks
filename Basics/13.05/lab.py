# role = "Administrator"
#
# if role != "Administrator":
#     print("No Permission!")
# else:
#     print("Welcome")



#Gender and age

gender_word = str(input())
age = int(input())

if gender_word == "f":
   print(gender_word)
   if age < 16:
       print("Miss")
   else:
       print("Ms.")

else:
    print(gender_word)
    if age < 16:
        print("Master")
    else:
        print("Mr.")