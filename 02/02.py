from random import randint

body = 0
with open('../priklady.txt', 'w') as file:
    for i in range(10):
        a, b = randint(0,10), randint(0,10)
        print(f'{a} * {b} = ', end=' ')
        file.write(f'{a} * {b} = \n')
        vysledok = int(input())
        if a*b == vysledok:
            body += 1

    print('Pocet bodov je ', body)
