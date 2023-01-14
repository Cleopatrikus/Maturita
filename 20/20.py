def bankomat(suma):
    delitelne = True
    try:
        int(suma)
    except ValueError:
        print('Zle zadanie sumy')
        bankomat(input('Suma: '))
    else:
        s = int(suma)
        sto, pat, dva, des = 0,0,0,0
        while s != 0:
            if s >= 100:
                sto += s // 100
                s -= 100*(s//100)
            elif s >= 50:
                pat += s // 50
                s -= 50*(s//50)
            elif s >= 20:
                dva += s // 20
                s -= 20*(s//20)
            elif s >= 10:
                des += s // 10
                s -= 10*(s//10)
            else:
                delitelne = False
                break
        if delitelne:
            print(f'stoviek {sto}, patdesiatok {pat}, dvadsiatok {dva}, desiatok {des}')
        elif not delitelne:
            print('Neda sa')

bankomat(input('Suma: '))

