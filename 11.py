teplota = []
def pocet_merani(subor):
    print(f'Pocet merani je {len(subor)}')


def najvyssia_teplota(subor):
    for i in subor:
        teplota.append(i.split(' ')[3].replace(',', '.'))
    teplota_float = [float(i) for i in teplota]
    print('Najvyssia namerana teplota je {}'.format(str(sorted(teplota_float, reverse=True)[0]).replace('.', ',')))

def priemerna_teplota(subor):
    for i in subor:
        teplota.append(i.split(' ')[3].replace(',', '.'))
    teplota_float = [float(i) for i in teplota]
    print('Priemerna teplota je {}'.format(str(round(sum(teplota_float)/len(teplota_float), 2)).replace('.', ',')))


with open('meteo_stanice.txt') as f:
    subor = f.readlines()
    pocet_merani(subor)
    najvyssia_teplota(subor)
    priemerna_teplota(subor)
