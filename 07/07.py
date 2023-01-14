import tkinter as tk
from random import randint

c = tk.Canvas(width=600, height=400)
c.pack()

body = 0
t1, t2 = '0', '0'

c.create_text(300, 20, text=f'Pocet bodov {body}', tags='body')
c.create_rectangle(200, 175, 250, 225)
c.create_rectangle(350, 175, 400, 225)
c.create_text(225, 200, text=t1, tags='t1')
c.create_text(375, 200, text=t2, tags='t2')


def casovac():
    global t1, t2

    t1 = str(randint(1, 6))
    t2 = str(randint(1, 6))

    c.itemconfig('t1', text=f'{t1}')
    c.itemconfig('t2', text=f'{t2}')

    c.after(850, casovac)


def rovnake():
    global t1, t2, body

    if t1 == t2:
        body += 2
    else:
        body -= 1

    c.itemconfig('body', text=f'Pocet bodov {body}')
    c.update()


casovac()

b1 = tk.Button(text='Rovnake', command=rovnake)
b1.pack()


tk.mainloop()
