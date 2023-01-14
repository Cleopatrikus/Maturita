import tkinter as tk

c = tk.Canvas(width=600, height=600)
c.pack()

c.create_line(10, 10, 10, 550)
c.create_line(10, 550, 600, 550)

def vysky():
    l = []
    while True:
        cislo_str = input('Zadajte cislo: ')
        try:
            int(cislo_str)
        except ValueError:
            print('Zadali ste neplatne cislo')
        else:
            cislo = int(cislo_str)
            if cislo < 0:
                break
            else:
                l.append(cislo)
    kresli(l)

def kresli(l):
    offset = 20
    for i, vyska in enumerate(l):
        c.create_rectangle(offset + (20 * i), 550, offset + (20 * (i + 1)), 550-(vyska * 50))
        c.create_text((offset + 10) * (20 * i), 570, text=f'{vyska}')
        offset += 10

vysky()

tk.mainloop()
