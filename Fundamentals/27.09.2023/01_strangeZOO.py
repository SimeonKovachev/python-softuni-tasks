tail = input()
body = input()
head = input()
full_pieces = [tail, body, head]

full_pieces[0], full_pieces[2] = full_pieces[2], full_pieces[0]

print(full_pieces)