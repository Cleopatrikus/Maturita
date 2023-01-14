from string import ascii_lowercase
with open('tabulka_pocetnosti.txt', 'r') as file:
    out = []
    file_read = file.read().lower()
    for i in ascii_lowercase:
        out.append(f'{i.upper()} - {file_read.count(i)}')
    for i in out:
        print(i)
