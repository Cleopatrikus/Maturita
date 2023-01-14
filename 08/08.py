import tkinter as tk
from random import randint, choice

c = tk.Canvas(width=600, height=400)
c.pack()

farby = ('red', 'green', 'blue')
c.create_text(0, 0, text='', tags='t1')
angle = 0


def casovac():
    global angle
    if e1.get() != '':
        c.delete('all')
        x, y = randint(50, 550), randint(20, 380)
        angle += 10
        if angle > 90:
            angle = 10
        c.create_text(x, y, text=e1.get(), fill=choice(farby), angle=angle)
    c.after(1250, casovac)

def m1(event):
    global angle
    c.delete('all')
    angle = 0


c.bind('<Button-1>', m1)
e1 = tk.Entry()
e1.pack()

casovac()

tk.mainloop()
