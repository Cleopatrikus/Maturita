mail = input("email: ")

split_on_at = mail.split("@")
split_on_dot = split_on_at[-1].split(".")

print(f'TLD: {split_on_dot[-1]}')
print(f'Server: {split_on_at[-1]}')
print(f'User: {split_on_at[0]}')
print(f'Domeny: \n'
      f'Domena 1 urovne: {split_on_dot[-1]}\n'
      f'Domena 2 urvone: {split_on_dot[-2]}\n'
      f'Domena 3 urvone: {split_on_dot[-3]}')
