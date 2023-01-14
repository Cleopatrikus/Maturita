cislo = input('Cislo: ')
sustava = int(input('Sustava: '))

print(f'Cislo je {int(cislo, sustava)}')

def prevod (cislo, sustava):
    x = 0
    for i in cislo:
        x *= sustava
        x += int(i)
        
    print(x)

prevod(cislo, sustava)