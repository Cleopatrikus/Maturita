import tkinter as tk

c = tk.Canvas(width=600, height=100, background='white')
c.pack()


def stlac(sur):
    global displej

    if sur.y >= 40 and sur.y < 70:
        cislica = sur.x // 30
        c.itemconfig(displej, text=cislica)


for i in range(10):
    c.create_rectangle(i * 30, 40, (i + 1) * 30, 70)
    c.create_text(i * 30 + 15, 55, text=i)

displej = c.create_text(3, 3, anchor='nw', font='Courier 30', text=0)
c.bind('<Button-1>', stlac)

tk.mainloop()