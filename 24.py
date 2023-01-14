from random import randint


def file_create():
    with open('hlasovanie_1.txt', 'w') as file:
        for i in range(50):
            file.write(str(randint(5224, 5227))+'\n')
        file.write(str(randint(5224, 5227)))


file_create()

with open('hlasovanie_1.txt', 'r') as file:
    pos = 0
    y = 0
    sutaziaci = [i for i in range(5224, 5227 + 1)]
    print(sutaziaci)
    lines = [int(i[:-1]) if i[-1] == '\n' else int(i) for i in file.readlines()]
    print(f'Pocet zaslanych SMS {len(lines)}')
    for i in sutaziaci:
        print(f'Pocet hlasov {i} je {lines.count(i)}')
    pos = lines.count(sutaziaci[0])
    for i in sutaziaci:
        if pos >= lines.count(i):
            pos = lines.count(i)
            minimum = i
    print(f'Najmenej hlasov dostal {minimum}')

