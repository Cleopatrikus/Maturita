import tkinter as tk
from random import randint

c = tk.Canvas(width=600, height=600)
c.pack()

c.create_oval(10, 10, 60, 60, fill='blue', tags='blue')
c.create_oval(540, 10, 590, 60, fill='red', tags='red')


def casovac():
    c.move('blue', randint(5, 10), 0)
    c.move('red', -randint(5, 10), 0)
    x, x1 = c.coords('blue')[2], c.coords('red')[0]
    if x > x1:
        c.create_text((x + x1) / 2, 70, text='Bum')
    else:
        c.after(50, casovac)


casovac()

tk.mainloop()
