farby = []


def pocet_jedal(subor):
    print(f'Pocet jedal je {len(subor)}')


def pocet_jednotlivych_jedal(subor):
    farby = []
    for i in subor:
        farby.append(i.split(' ')[1])
    farby = [i[:-1] if i[-1] == '\n' else i for i in farby]
    #print(farby)
    z, c, m, o = farby.count('z'), farby.count('c'), farby.count('m'), farby.count('o')
    print('Pocet jedal je z = {}, c = {}, m = {}, o = {}'.format(z, c, m, o))


def menej_ako_20(subor):
    farby = []
    for i in subor:
        farby.append(i.split(' ')[1])
    farby = [i[:-1] if i[-1] == '\n' else i for i in farby]
    z, c, m, o = farby.count('z'), farby.count('c'), farby.count('m'), farby.count('o')
    if z < 20:
        print('z je menej ako 20')
    if c < 20:
        print('c je menej ako 20')
    if m < 20:
        print('m je menej ako 20')
    if o < 20:
        print('o je menej ako 20')


def dostatocny_pocet(subor):
    farby = []
    for i in subor:
        farby.append(i.split(' ')[1])
    farby = [i[:-1] if i[-1] == '\n' else i for i in farby]
    z, c, m, o = farby.count('z'), farby.count('c'), farby.count('m'), farby.count('o')
    if z > 2:
        print('z je viac ako 2')
    if c > 2:
        print('c je viac ako 2')
    if m > 2:
        print('m je viac ako 2')
    if o > 2:
        print('o je viac ako 2')


with open('objednane_jedla.txt') as f:
    subor = f.readlines()
    pocet_jedal(subor)
    pocet_jednotlivych_jedal(subor)
    menej_ako_20(subor)
    dostatocny_pocet(subor)
