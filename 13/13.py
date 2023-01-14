import tkinter as tk

c = tk.Canvas(width=1000, height=600)
c.pack()

p = 20
s = 80

for i in range(5):
    for j in range(5):
        c.create_rectangle(p + (s * i), p + (s * j), p + (s * (i + 1)), p + (s * (j + 1)), tag='pole')

c.create_text(700, 50, text='Piškvorky', font='Arial 40', fill='green')
c.create_text(750, 150, text='Vyhráva ten, kto má 4 znaky vedľa seba v jednom z poradi: vodorovne, zvislo, diagonálne\n'
              'hráči sa po každom ťahu striedajú\n'
              'Tri hracie polia\n'
                            '       4x4 stlačením klávesu 4\n'
                            '       5x5 stlačením klávesu 5\n'
                            '       6x6 stlačením klávesu 6\n')


def M1_down(event):
    x = event.pos
    y = event.y
    c.create_rectangle(x - 15, y - 15, x + 15, y + 15, fill='blue')
    c.update()


def M3_down(event):
    x = event.pos
    y = event.y
    c.create_oval(x - 15, y - 15, x + 15, y + 15, fill='purple')
    c.update()


def key_4_down(event):
    c.delete('all')
    c.create_text(700, 50, text='Piškvorky', font='Arial 40', fill='green')
    c.create_text(750, 150,
                  text='Vyhráva ten, kto má 4 znaky vedľa seba v jednom z poradi: vodorovne, zvislo, diagonálne\n'
                       'hráči sa po každom ťahu striedajú\n'
                       'Tri hracie polia\n'
                       '       4x4 stlačením klávesu 4\n'
                       '       5x5 stlačením klávesu 5\n'
                       '       6x6 stlačením klávesu 6\n')
    for i in range(4):
        for j in range(4):
            c.create_rectangle(p + (s * i), p + (s * j), p + (s * (i + 1)), p + (s * (j + 1)), tag='pole')


def key_5_down(event):
    c.delete('all')
    c.create_text(700, 50, text='Piškvorky', font='Arial 40', fill='green')
    c.create_text(750, 150,
                  text='Vyhráva ten, kto má 4 znaky vedľa seba v jednom z poradi: vodorovne, zvislo, diagonálne\n'
                       'hráči sa po každom ťahu striedajú\n'
                       'Tri hracie polia\n'
                       '       4x4 stlačením klávesu 4\n'
                       '       5x5 stlačením klávesu 5\n'
                       '       6x6 stlačením klávesu 6\n')
    for i in range(5):
        for j in range(5):
            c.create_rectangle(p + (s * i), p + (s * j), p + (s * (i + 1)), p + (s * (j + 1)), tag='pole')


def key_6_down(event):
    c.delete('all')
    c.create_text(700, 50, text='Piškvorky', font='Arial 40', fill='green')
    c.create_text(750, 150,
                  text='Vyhráva ten, kto má 4 znaky vedľa seba v jednom z poradi: vodorovne, zvislo, diagonálne\n'
                       'hráči sa po každom ťahu striedajú\n'
                       'Tri hracie polia\n'
                       '       4x4 stlačením klávesu 4\n'
                       '       5x5 stlačením klávesu 5\n'
                       '       6x6 stlačením klávesu 6\n')
    for i in range(6):
        for j in range(6):
            c.create_rectangle(p + (s * i), p + (s * j), p + (s * (i + 1)), p + (s * (j + 1)), tag='pole')


c.bind('<Button-1>', M1_down)
c.bind('<Button-3>', M3_down)

c.bind_all('<Key-4>', key_4_down)
c.bind_all('<Key-5>', key_5_down)
c.bind_all('<Key-6>', key_6_down)


tk.mainloop()
