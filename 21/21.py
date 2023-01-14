from random import randint, randrange
from string import ascii_lowercase


def vytvorenie_mien():
    with open('sutaz_vbehu.txt', 'w') as file:
        for i in range(32):
            x = ascii_lowercase[randrange(len(ascii_lowercase))].upper()
            for i in range(randint(5, 12)):
                x += ascii_lowercase[randrange(len(ascii_lowercase))]
            x += f' {randint(200, 400)}\n'
            file.write(x)

# vytvorenie_mien()


with open('sutaz_vbehu.txt', 'r') as file:
    lines = [i[:-1] if i[-1] == '\n' else i for i in file.readlines()]
    times = []
    print(f'Pocet zucastnenych sportovcov: {len(lines)}')
    for i in lines:
        name = i.split(' ')[0]
        time = i.split(' ')[1]
        times.append(int(time))
        print(f'Sutaziaci {name} dobehol do ciela za {time} sekund')
    cas_vitaza = sorted(times)[0]
    print(f'Vitaz je {[i for i in lines if str(cas_vitaza) in i][0].split(" ")[0]}, '
          f's casom {cas_vitaza // 60} minuty a {cas_vitaza - cas_vitaza // 60 * 60} sekund')
