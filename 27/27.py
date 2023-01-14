from random import choice

stud = int(input('Stud:'))
otaz = int(input('Otaz:'))

stud_list = [i+1 for i in range(stud)]
otaz_list = [i+1 for i in range(otaz)]

i = 1
if stud <= otaz:
    while stud_list != []:
        r_stud = choice(stud_list)
        r_otaz = choice(otaz_list)
        stud_list.remove(r_stud)
        otaz_list.remove(r_otaz)
        print(f'{i}. student: {r_stud}, otazka {r_otaz}')
        i += 1
else:
    print('Pocet otazok je mensi ako pocet studentov')
