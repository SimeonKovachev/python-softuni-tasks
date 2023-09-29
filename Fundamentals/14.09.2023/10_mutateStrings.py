first_word = str(input())
second_word = str(input())
last_printed_word = first_word

for index in range(len(first_word)):
    left_part = second_word[:index + 1]
    right_part = first_word[index + 1:]
    new_word = left_part + right_part

    if new_word == last_printed_word:
        continue
    print(new_word)
    last_printed_word = new_word

