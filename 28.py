with open('prihlaseni.txt', 'r') as file:
    pod_15 = []
    lines = [i.strip() for i in file.readlines()]
    print(f'Pocet prihlasenych je {len(lines)/2}')
    for i, value in enumerate(lines):
        try:
            int(value)
        except ValueError:
            pass
        else:
            lines[i] = int(value)
    for i, value in enumerate(lines):
        if type(value) == int:
            if value < 15:
                print(lines[i-1], end=' ')
                pod_15.append(value)
    print()

    cena = float(input('Cena: '))
    cestovne = 0
    for i in (lines):
        if type(i) == str:
            if i in pod_15:
                cestovne += cena / 2
            cestovne += cena
    print(cestovne)

    vek = 0
    for i in lines:
        if type(i) == int:
            vek += i
    print(vek)
    print(f'Priemerny vek je {round (vek / (len(lines)/2), 2)}')
