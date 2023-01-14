import tkinter as tk

c = tk.Canvas(width=600, height=600)
c.pack()


def M1(event):
    x = event.x
    y = event.y
    e1 = entry1.get()
    e2 = entry2.get()
    c.create_rectangle(x-50,y-20,x+50,y+20)
    c.create_text(x, y, text=e1, font='50')
    c.create_rectangle(x-5,y+20, x+5, y+100, fill='grey', width=0)
    if e2 == 'k':
        c.create_line(x-50, y+20, x+50, y-20, fill='grey', width = 2)


def d():
    c.delete('all')


c.bind('<Button-1>', M1)

entry1 = tk.Entry()
entry1.pack()

entry2 = tk.Entry()
entry2.pack()

button2 = tk.Button(text='Delete', command=d)
button2.pack()

tk.mainloop()
